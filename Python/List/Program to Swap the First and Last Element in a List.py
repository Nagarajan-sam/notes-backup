n=[1,2,3,4,5,6]
length=len(n)
temp=n[0]
n[0]=n[length-1]
n[length-1]=temp
print(n)
