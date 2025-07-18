a=int(input("Enter the amount to be stored: "))
deno=[500, 200, 100, 50, 20, 10, 5, 2, 1]
cash=[]
for i in deno:
    temp=a//i
    a=a-(temp*i)
    cash.append((i,temp))
print("Money---Notes")
for i,temp in cash:
    if(temp!=0):
        print(i,temp)