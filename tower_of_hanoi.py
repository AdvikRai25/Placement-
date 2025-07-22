def toh(n, s, a, t):
    if n == 1:
        print("Move {} from {} to {}".format(n, s, t))
        return
    toh(n-1, s, t, a)
    print("Move {} from {} to {}".format(n, s, t))
    toh(n-1, a, s, t)

n = int(input("Enter any number: "))
toh(n, "A", "B", "C")
