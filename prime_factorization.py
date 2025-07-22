def prime_factors(n):
    for i in range(2, n+1):
        if n % i == 0:
            print(i, end=" ")
            prime_factors(n // i)
            break

n = int(input("Enter any number: "))
prime_factors(n)


