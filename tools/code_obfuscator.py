from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout

import random
import string
import re

filename = input("Type in the filename you want to obfuscate (no file extension): ")
with suppress_stdout():
    new_module = __import__(filename)

f = open(f"{filename}.py", "r")
file = f.read()
f.close()

#find variable names
variable_names = [v for v in dir(new_module) if not v.startswith("__")]

obfuscated_names = []

for i in range(len(variable_names)):
    obfuscated_names.append(''.join(random.choices(string.ascii_letters, k=15)))

# change var names
file = "\n" + file
for i in range(len(variable_names)):
    file = re.sub(r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_names[i], file)


# add dummy variables
def randVar():
    return "".join(random.choices(string.ascii_letters, k=15))
def randData(t):
    if t == "string":
        t = ''.join(random.choices(string.ascii_letters, k=15))
        t =  f"\"{str(t)}\""
    elif t == "int":
        t = random.randint(1,100000)
    return t


# replace all strings with their hex representation
for i in re.findall(r"(\".*\"|'.*')",file):
    s = i[1:-1]
    file = re.sub(i,f"bytes.fromhex(\'{s.encode('utf-8').hex()}\').decode('utf-8')",file)

#functions for dummy random code generation

def genFillerCode(num_lines, indent, max_depth):
    code = '\n'
    for num in range(random.randint(1, num_lines)):
        statement = genFillerStatements(indent, max_depth)
        code += f'{statement}\n'
    return code

def genFillerStatements(indent, max_depth):
    statements = [
        " "*indent + f'{randVar()} = {randData("int")}',
        " "*indent + f'{randVar()} = {randData("string")}',
    ]
    if max_depth > 1:
        statements.append(genFor(indent, max_depth - 1))
        statements.append(genIf(indent, max_depth - 1))
        # statements.append(genWhile(indent, max_depth - 1)) 
    choice = random.choice(statements)
    return choice

# inject if conditionals

def genIf(indent, max_depth): 
    if max_depth > 0:
        variable1 = randVar() 
        variable2 = randVar()
        conditionals = [
            '==',
            '!=',
            '>=',
            '<='
        ]
        code = "\n" +" "*indent + f'{variable1} = {randData("int")}\n'
        code += " "*indent + f'{variable2} = {randData("int")}\n'
        code += " "*indent + f'if {variable1} {random.choice(conditionals)} {variable2}:\n' 
        code += genFillerCode(4, indent+4, max_depth - 1)
        
        return code 
    else: 
        return " "*(indent+4) + f'{randVar} = {randData}'

# inject for loops

def genFor(indent, max_depth):
    if max_depth > 0:
        code = " "*indent + f'for {chr(97 + indent)} in range({random.randint(3,8)}):\n'
        code += genFillerCode(4, indent+4, max_depth - 1)
        return code
    else:
        return " "*(indent+4) + f'{randVar} = {randData}'

# inject while loops (scrapped because variables would not cooperate)

# def genWhile(indent, max_depth):
#     conditionals = [
#             '==',
#             '!=',
#             '<=',
#         ]
#     if max_depth > 0:
#         variable = chr(97+indent)
#         code = " "*indent + f'while {variable} {random.choice(conditionals)} {random.randint(1,3)}:\n'
#         code += genFillerCode(4, indent+4, max_depth -1 )
#         code += " "*(indent+4) + f'{variable} += 1' + '\n'
#         return code
#     else: 
#         return " "*(indent+4) + f'{randVar} = {randData}'


def insertDummy(file):
    output = ""
    file = file.split("\n")
    for i in range(len(file)):
        line = file[i]
        hasIf = re.search(r'\bif\s+.+:', line)
        hasLoop = re.search(r'\bfor\s+.+:', line) or re.search(r'\bwhile\s+.+:', line)
        if hasIf or hasLoop:
            currentIndent = len(line) - len(line.lstrip(' '))
            output += genFillerCode(random.randint(1,4),currentIndent, 5)
            output += f"\n{line}"
        else:
            output += f"\n{line}"
    return output


#insert unused functions
def genFunctions(function_name):
    code = f'def {function_name}'
    code += genFillerCode(random.randint(0,5), 1)
    return code

def oneLineify(file):
    output = ""
    file = file.strip()
    file = file.split("\n")
    for i in range(len(file)):
        line = file[i]
    # pserb was here
        nextIndent = 0
        currentIndent = len(line) - len(line.lstrip(' '))
        if i < len(file) - 1:
            nextIndent = len(file[i+1]) - len(file[i+1].lstrip(' '))
        
        hasConditional = re.search(r'\bif\s+.+:', line) or re.search(r'\belif\s+.+:', line) or re.search(r'\belse:', line)
        hasLoop = re.search(r'\bfor\s+.+:', line) or re.search(r'\bwhile\s+.+:', line)
        if hasConditional or hasLoop:
            output += f"\n{line}\n"
        elif currentIndent > nextIndent:
            output += f"{line}\n"
        elif line == "":
            output += line.lstrip(" ")
        else:
            output += f"{line};"
    
    return output


def removeWhitespace(file):
    output = ""
    file = file.split("\n")
    for line in file:
        hasConditional = re.search(r'\bif\s+.+:', line) or re.search(r'\belif\s+.+:', line) or re.search(r'\belse:', line)
        hasLoop = re.search(r'\bfor\s+.+:', line) or re.search(r'\bwhile\s+.+:', line)
        currentIndent = len(line) - len(line.lstrip(' '))
        if hasConditional or hasLoop:
            parts = line.split(":")
            output += "\n" + parts[0] + ":"
            output += "".join(parts[1].split())
        elif line == "":
            pass
        else:
            output += "\n" + " "*currentIndent
            output += "".join(line.split())

    output = output.strip()
    return output
        
if not (os.path.exists("out")):
    os.makedirs("out")
outfile = open(f"out/{filename}_obfuscated.py", "w")
outfile.write(removeWhitespace(oneLineify(insertDummy(file))))
# outfile.write(insertDummyIf(file))
# outfile.write(oneLineify(file))
outfile.close()

print(f"wrote to out/{filename}_obfuscated.py")
