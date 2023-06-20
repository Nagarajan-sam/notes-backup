d={'a':1,'b':2,'c':3,'d':4}
rm=input("enter the key values")
if rm in d:
    del d[rm]
else:
    print("not a valid key")
print(d)
