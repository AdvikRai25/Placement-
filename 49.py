class college:
    col="NITTE"
    def student(self,name,mark):
        self.name = name
        self.mark = mark
    def passfail(self):
        if(self.mark>40):
            print("clear")
        else:
            print("fail")
    def modify(self,grace):
        self.mark=self.mark+grace
    def display(self):
        print("Name ",self.name)
        print("College",self.col)
        print("Mark ",self.mark)
        self.passfail()
s1=college()
s2=college()
s1.student("Adam",39)
s2.student("Advik",90)
s1.modify(1)
s1.display()
print("________________________")
s2.display()
#If u want to use methods or variables we have to use class name or object name in main part

