def climb(x, A, D):
    if A >= x:
        return 1
    time = 0
    height = 0
    while True:
        time += 1
        height += A
        if height >= x:
            return time
        time += 1
        height -= D
x = 25
A = 7
D = 4
print("Minimum time to reach the top:",climb(x, A, D))
