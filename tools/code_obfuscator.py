import test
import random
import string
import re

f = open("test.py", "r")
file = f.read()
f.close()

variable_names = [v for v in dir(test) if not v.startswith("__")]

obfuscated_names = []

for i in range(len(variable_names)):
    obfuscated_names.append(''.join(random.choices(string.ascii_letters, k=15)))

#print(obfuscated_names)


# change var names
file = "\n" + file
for i in range(len(variable_names)):
    file = re.sub(r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_names[i], file)


# add dummy variables
file = file.split("\n")
for _ in range(random.randint(50,100)):

    randstr = ''.join(random.choices(string.ascii_letters, k=15)) + " "*random.randint(2,20) + "=" + " "*random.randint(2,10) + "5"
    file.insert(random.randint(0,len(file)-1),randstr)

file = "\n".join(file)


for i in re.findall(r"(\".*\"|'.*')",file):
    print(i)
    string = i[1:-1]
    file = re.sub(i,f"bytes.fromhex(\'{string.encode('utf-8').hex()}\').decode('utf-8')",file)

print(file)

# insert unused functions

# inject if conditionals

# remove all spaces
file = file.split("\n")
print(file)
for line in file: 
    if line == '': 
        file.remove(line) 
file = "\n".join(file)
print(file)