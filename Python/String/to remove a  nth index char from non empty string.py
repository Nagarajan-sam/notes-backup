a=input("enter the string")
index=6
n=len(a)
new=""
i=0
while (i<n):
    if(i!=index):
        new+=a[i]
    i=i+1
print(new)
