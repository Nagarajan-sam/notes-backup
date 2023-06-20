a="hai how are you"
res=""
for i in range(len(a)):
    if (a[i]== " "):
        res=res+ "_"
    else:
        res=res+a[i]
print(res)
