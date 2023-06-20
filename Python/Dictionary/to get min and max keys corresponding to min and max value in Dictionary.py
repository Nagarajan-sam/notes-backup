def test(d):
    return max(d,key = d.get) ,min(d,key = d.get) #to find the min and max value of key 
fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}    
print("the original dictionary")
print(fruitsDict)
print("the maximum and minimum val in dictionary",test(fruitsDict))
