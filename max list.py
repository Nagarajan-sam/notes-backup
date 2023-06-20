def max(list):
    max=list[0]
    for a in list:
        if a > max :
            max=a
    return max
print(max([10,20,50,70]))
