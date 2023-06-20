def len_words(mylist):
    c=0
    for item in mylist:
        if len(item)>c:
            c=len(item)
    return c
print(len_words(["hello","goodmorning","hai"]))
