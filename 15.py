a=10
for i in range(1,5):
    for j in range(i):
        a=a+i
    a=a-2
    print(a,end="")
print(a)