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

def genFillerCode(num_lines, indents):
    code = ''
    for num in range(num_lines):
        statement = genFillerStatements()
        code += '    '*indents + f'{statement}\n'
    return code

def genFillerStatements():
    statements = [
        f'{randVar()} = {randData("int")}',
        f'{randVar()} = {randData("string")}'
    ]
    return random.choice(statements)

# inject if conditionals into while loops

def genIf(): 
    variable1 = randVar() 
    variable2 = randVar()
    conditionals = [
        '==',
        '!=',
        '>=',
        '<='
    ]
    code = f'\n{variable1} = {randData("int")} \n{variable2} = {randData("int")} \n'
    code += f'if {variable1} {random.choice(conditionals)} {variable2}:\n' 
    code += genFillerCode(random.randint(2,4), 1)
    return code 

def insertDummyIf(file):
    output = ""
    file = file.split("\n")
    for i in range(len(file)):
        line = file[i]
        hasConditional = re.search(r'^if\s+.+:', line)
        if hasConditional:
            output += genIf()
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
    # for line in file:
        hasConditional = re.search(r'if\s+.+:', line) or re.search(r'elif\s+.+:', line) or re.search(r'else\s+.+:', line)
        if hasConditional:
            output += f"\n{line}"
        elif (line[0:4] == "    ") and (i < len(file)-1) and (file[i+1][0:4] != "    "):
            output += f"{line}\n"
        elif line == "":
            output += line
        else:
            output += f"{line};"
    
    return output

def removeWhitespace(file):
    output = ""
    file = file.split("\n")
    for line in file:
        if line[0:3] == "if ":
            parts = line.split("if ")
            output += "\nif "
            output += "".join(parts[1].split())
        elif line[0:5] == "elif ":
            parts = line.split("elif ")
            output += "\nelif "
            output += "".join(parts[1].split())
        elif line[0:5] == "else ":
            parts = line.split("else ")
            output += "\nelse "
            output += "".join(parts[1].split())
        elif line == "":
            pass
        else:
            output += "\n"
            output += "".join(line.split())

    output = output.strip()
    return output
    
        

# remove all spaces
file = file.split("\n")

for line in file: 
    if line == '': 
        file.remove(line) 
file = "\n".join(file)

if not (os.path.exists("out")):
    os.makedirs("out")
outfile = open(f"out/{filename}_obfuscated.py", "w")
outfile.write(removeWhitespace(oneLineify(insertDummyIf(file))))
# outfile.write(insertDummyIf(file))
# print(removeWhitespace(oneLineify(file)))
outfile.close()

print(f"wrote to out/{filename}_obfuscated.py")
