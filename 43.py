def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def cop(a, b):
    return gcd(a, b) == 1

num = int(input("Enter any number: "))
for i in range (1, num):
    for j in range(1, i):
        for k in range (1, j):
            if j*j + k*k == i*i and cop(i, j) and cop(j,k) and cop(i, k):
                print(k, j, i)