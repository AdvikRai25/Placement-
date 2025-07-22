class LC37:
    def rectangle(self):
        self.length = int(input("Enter length: "))
        self.breadth = int(input("Enter breadth: "))

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def display(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())


s1 = LC37()
s2 = LC37()

print("Enter dimensions for rectangle 1:")
s1.rectangle()

print("\nEnter dimensions for rectangle 2:")
s2.rectangle()

print("\nRectangle 1:")
s1.display()

print("------------")

print("Rectangle 2:")
s2.display()
