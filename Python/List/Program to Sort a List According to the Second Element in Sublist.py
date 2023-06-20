def second_ele(sublist):
    return sublist[1]

mylist=[[4,5,50],[1,2,3,100],[60,90],[7,8,9,10]]
newlist= sorted(mylist,key=second_ele)
print(newlist)
