n=int(input("enter the values"))
d={}
for i in range(n):
    k=input("enter the key")
    v=int(input("enter the values"))
    d.update({k:v})
print(d)
print(d.values())
dval=sum(d.values())
print(dval)
