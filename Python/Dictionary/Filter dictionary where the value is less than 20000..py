empdict = {'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
print("original dictionary")
print(empdict)
print("filter dictionary where the value is less than 20000")
result = {key:values for (key,values) in empdict.items() if values < 20000}
print(result)
