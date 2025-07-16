names = []
for i in range(5):
    a = input("Enter your name {}: ".format(i + 1))
    names.append(a)

index = 1
for name in names:
    print("{}. Mr/Ms {}".format(index, name))
    index += 1
