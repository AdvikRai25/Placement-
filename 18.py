head = int(input("Enter number of heads: "))
legs = int(input("Enter number of legs: "))
for h in range(head + 1):
    c = head - h
    if (2 * h + 4 * c)== legs:
        print("Hens:", h)
        print("Cows:", c)
        break
else:
    print("No solution")
