mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
print("Original Dictionary:")
print(mutidict)
print("New Dictionary after dropping empty items:")
d= {key:value for (key, value) in mutidict.items() if value is not None}
print(d)
