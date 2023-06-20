inp=int(input('enter the number :'))
tot_number=[]
for i in range(0,inp):
    tot_number.append(int(input("number to add:")))
lar_even=0
lar_odd=0
for i in range (0,inp):
    if (tot_number[i] % 2 == 0 and tot_number[i] > lar_even):
        lar_even=tot_number[i]
    elif(tot_number[i]%2 != 0 and tot_number[i] > lar_odd):
        lar_odd=tot_number[i]
print("largest even number:", lar_even)
print("largest odd number:", lar_odd)
