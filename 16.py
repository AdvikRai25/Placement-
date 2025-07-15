a=int(input("Enter number of rows: "))
for i in range(a):
    for i in range(a-i):#(i-1)
        print("*",end=" ")
    print()