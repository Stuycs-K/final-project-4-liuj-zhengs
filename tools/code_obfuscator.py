import test
import random
import string

f = open("test.py", "r")
file = f.read()
f.close()

variable_names = [v for v in dir(test) if not v.startswith("__")]

obfuscated_names = []

for i in range(len(variable_names)):
    obfuscated_names.append(''.join(random.choices(string.ascii_letters, k=15)))

#print(obfuscated_names)

def valid_var(s,tok):
    s = s.strip()
    if s[s.index(tok)+1] == "=" or s[s.index(tok)+1] == "," or s[s.index(tok)+1] == ")" or s[s.index(tok)+1] == ".":
        return True
    return False


        



