a=int(input("Enter number 1"))
b=int(input("Enter number 2"))
if(a>b):
    big=a
else:
    big=b
step=big
while(True):
    if(big%a==0 and big %b==0):
        print(big)
        break
    else:
        big=big+step