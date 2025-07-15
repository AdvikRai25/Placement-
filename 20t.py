rows = int(input("Enter number of rows: "))
num = 1
for i in range(1, rows + 1):
    if i % 2 == 1:
        for j in range(1, i + 1):
            print(num, end="")
            num += 1
            if j != i:
                print("*", end="")
    else:
        temp = num + i - 1
        for j in range(1, i + 1):
            print(temp, end="")
            temp -= 1
            if j != i:
                print("*", end="")
        num += i
    print()
