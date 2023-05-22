import test
import random


variable_names = [v for v in dir(test) if not v.startswith("__")]

obfuscated_names = []

for i in range(variable_names):
    obfuscated_names.append(''.join(random.choices(string.ascii_letters, k=N)))

print(obfuscated_names)
