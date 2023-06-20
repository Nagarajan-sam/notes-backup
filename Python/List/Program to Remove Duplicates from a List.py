mylist=[1,2,3,2,1,5,2]
l=[]
for item in mylist:
    if item not in l:
        l.append(item)
print(l)
