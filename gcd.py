a=int(input("Enter number 1"))
b=int(input("Enter number 2"))
c=0
while(b!=0):
    c=a%b
    a=b
    b=c
print(a)