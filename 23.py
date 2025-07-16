a=[[[11,22,33],
    [44,55,66],
    [77,12,32]],

    [[41,42,43],
    [52,54,56],
    [98,97,95]]]
for i in range(2):
    for j in range(3):
        for k in range(3):
            print(a[i][j][k],end=" ")
        print()
    print("_________________________")