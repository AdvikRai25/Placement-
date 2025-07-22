def rcb():
    return len([[2, 3], [5, 6, 7]])

def csk():
    raj = [3, 4, 5]
    return raj[1]

def mi(a):
    return len(str(a))

def GT(s):
    d = list(s)
    return len([i for i in d if i in "aeiou"])

a = GT("gill")

for i in range(rcb()):
    a = a + csk()

print(a * mi(3))  
