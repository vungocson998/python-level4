# D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# NOT A SEQUENCE BUT MAPPING(key-value)
# Basic functions: keys(), values(), get(), pop(), ...
# Using dictionary in for loop
# Missing key if test



D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
keys = list(D.keys())
values = list(D.values())

print(D.get("food"))
print(D)

print(D.pop("food"))
print(D)

keys.sort()
print(keys)

D['new-key'] = "TED"
print(D)

# Using dictionary in for loop
for key in D:
    print(key, "=>", D[key])

# Missing key if test
if not "f" in D:
    print("Missing")



