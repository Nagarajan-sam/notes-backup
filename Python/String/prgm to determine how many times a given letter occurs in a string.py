str="python programming"
c=input("enter the letter: ")
count=0
for i in str:
    if (i==c):
        count=count+1
print(c,"occurs",count,"times")
