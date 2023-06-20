n1=int(input("enter the number"))
l=[]
for i in range (n1):
    l.append(int(input("enter the numbers")))
print(l)
n2=int(input("enter the number"))
lis=[]
for j in range(n2):
    lis.append(int(input("enter the number")))
print(lis)
m= l + lis
print("merging list is :", m)
m.sort()
print("the sorted one is :",m)
