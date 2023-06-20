d={"Rahul":"developer","Tina":"Trainer","sam":"seo","Madhu":"developer"}
user_input=input("enter the key name")
if user_input in d:
    print("the key is present")
    print("the value of the key is",d[user_input])
else:
    print("the key is not present")
