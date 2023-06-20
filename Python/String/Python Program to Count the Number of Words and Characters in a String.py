str="python programming language"
ch=0 #taking this as words
word=1 #taking this as space
for i in str:
    ch=ch+1
    if (i==' '):
        word=word+1
print("thee total number of ch :", ch)
print("the total number of word :", word)
