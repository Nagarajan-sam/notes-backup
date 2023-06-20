def listsum(x):
    if len(x)==0:
        return 0
    else:
        return x[0] +listsum(x[1: :])
k=[11,22,33,44]
sum= listsum(k)
print("sum of list element is :", sum)
