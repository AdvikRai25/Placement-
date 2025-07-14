a=int(input("enter any num"))
total=0
while(a>0):
    total=total+a%10
    a=a//10
print("the sum of digits is",total)

