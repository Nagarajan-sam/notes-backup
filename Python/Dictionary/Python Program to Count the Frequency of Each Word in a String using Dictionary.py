str=input("enter the string")
split=str.split()
d={}
for word in split:
    d[word]=d.get(word,0) + 1 #geting that word and reading the current frecy value,the crnt fre val is not avail so 0
for key in sorted(d):
    print("{} : {}".format(key,d[key]))
