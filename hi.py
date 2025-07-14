a=10
for i in range(50):
    if(i%2==0 or i%3==0 or i%5==0 or i%7==0):
        continue
    print("hi")
    a=a+2
print(a)