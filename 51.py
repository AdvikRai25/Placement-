class rect:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def area(self):
        return self.a*self.b

nums = []
d = int(input("Enter the number of rectangles: "))
iii=1
for i in range(d):
    r = rect(i+10,i+20)
    nums.append(r)

for i in nums:
    print("area of rectangle {} : {}".format(iii,i.area()))
    iii=iii+1




