def circle(radius):
    return 3.14 * radius * radius

def square(side):
    return side * side

def triangle(base, height):
    return 0.5 * base * height

def rectangle(breadth, length):
    return length * breadth

while True:
    print("\n1. Circle")
    print("2. Square")
    print("3. Triangle")
    print("4. Rectangle")
    print("5. Exit")

    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            radius = float(input("Enter radius: "))
            res = circle(radius)
            print("Area of circle:", res)
        case 2:
            side = float(input("Enter side: "))
            res = square(side)
            print("Area of square:", res)
        case 3:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            res = triangle(base, height)
            print("Area of triangle:", res)
        case 4:
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            res = rectangle(breadth, length)
            print("Area of rectangle:", res)
        case 5:
            print("Exit")
            break
        case _:
            print("Invalid choice.")
