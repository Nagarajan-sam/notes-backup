string=input('enter the  string :')
final=""
for i in range(len(string)):
    if (i%2==0):
        final+=string[i]
print(final)
