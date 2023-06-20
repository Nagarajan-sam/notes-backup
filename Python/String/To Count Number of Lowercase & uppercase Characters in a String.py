s="MSYS technologies"
x,y=0,0
for i in s:
    if (i >= 'a' and i <= 'z'):
        x=x+1
    if (i >= 'A' and i <= 'Z'):
        y=y+1
print("the lowecase char is :", x)
print("the uppercase char is :", y)
