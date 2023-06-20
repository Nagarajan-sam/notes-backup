n=int(input("enter the numbers"))
l=[]
for i in range(n):
    l.append(int(input("enter the number")))
even=0
odd=0
neg=0

for j in l:
    if (j>0):
        if (j%2==0):
            even=even+j
        else:
            odd=odd+j
    else:
        neg=neg+j
print("the sum of even :", even)
print('the sum of odd :', odd)
print("the sum of neg :", neg)
