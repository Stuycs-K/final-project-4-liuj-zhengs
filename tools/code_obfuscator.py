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
for i in range(random.randint(50,100)):
    randstr = str(i) + " "*random.randint(2,10) + "=" + " "*random.randint(2,10) + "poop"
    file.insert(random.randint(0,len(file)-1),randstr)

file = "\n".join(file)
print(file)

