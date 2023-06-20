n=int(input("enter the number"))
l=[]
l_even=[]
l_odd=[]
for i in range(n):
    l.append(int(input('enter the number')))
print(l)
for i in l:
    if (i%2==0):
        l_even.append(i)
    else:
        l_odd.append(i)
print("even number:", l_even)
print("odd number:", l_odd)
