str = input("enter the string")
c=0
for i in str:
    if i in "a,e,i,o,u,A,E,I,O,U":
        c=c+1
print("the number of vowels :", c)
