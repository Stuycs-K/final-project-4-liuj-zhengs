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
def find(text,s):
    indexes = []
    index = 0
    while index + len(s)-1 < len(text):
        if text[index:index+len(s)] == s:
            indexes.append(index)
        index+=1
    



file = "\n" + file
for i in range(len(variable_names)):
    file = re.sub(r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_names[i], file)

print(file)


