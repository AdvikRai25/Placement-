a = int(input("Enter number of blocks: "))
b = int(input("Enter number of lines: "))
c = int(input("Enter number of stars per line: "))
count = 0
for i in range(a):
    print("----------- block", i + 1, "----------")
    for j in range(b - i):
        for k in range(c):
            print("*", end=" ")
            count += 1
        print()
    print(count)
    count=0
