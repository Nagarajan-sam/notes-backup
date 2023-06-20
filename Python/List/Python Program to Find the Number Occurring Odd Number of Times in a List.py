def odd_occu(mylist):
    for item in mylist:
        if mylist.count(item)%2!=0: #it will check that how many times the item is takes place
            return item
print(odd_occu([1,1,2]))
