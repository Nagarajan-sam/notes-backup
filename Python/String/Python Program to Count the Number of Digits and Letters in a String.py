digits=['1','2','3','4','4','5','6','7','8','9']
words=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
        'v','x','y','z']

str="gokul12345"
c1=0
c2=0
for i in str:
    if i in digits:
        c1=c1+1
    if i in words:
        c2=c2+1
print("words :", c1)
print("number :", c2)
