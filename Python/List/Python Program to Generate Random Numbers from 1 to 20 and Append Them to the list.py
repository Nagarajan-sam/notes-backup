import random
n=int(input('enter the total elements:'))
l=[]
for i in range(1,n+1):
    rn=random.randint(1,20)
    l.append(rn)
print('mylist of rn number:',l)
l.sort()
print(l)
