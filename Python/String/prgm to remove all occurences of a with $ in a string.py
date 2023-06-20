str="An apple A day keeps doctor away"
res=""
for i in range(0, len(str)):
    if (str[i] == 'a'  ):
        res=res+ '$'
    else:
        res=res+str[i]
print(res)
