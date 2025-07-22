def prime_factors(n):
    if n == 1:
        return
    i = 2
    while n%1 != 0:
        i += 1
    print(i, end=" ")
    prime_factors(n//i)
        
n = int(input("Enter any number: "))
prime_factors(n)


