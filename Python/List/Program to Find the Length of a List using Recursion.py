len=0
def length(a):
    global len
    if a:
        len=len+1
        length(a[1:])
    return len
mylist=[1,2,3,4,5]
len=length(mylist)
print("length :", len)
