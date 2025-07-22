class emp:
    profit=1000000
    tax=10
    company="TCS"
    def __init__(self,name,sal,age,per):
        self.name=name
        self.sal=sal
        self.age=age
        self.per=per
    def cal_tax(self):
        return (emp.tax/100)*self.sal
    def cal_share(self):
        return (self.per/100)*emp.profit
    def display(self):
        print("1.",self.name)
        print("2.",emp.company)
        print("3.",self.sal)
        print("4.",self.age)
        print("5.",self.per)
        print("6.",self.cal_tax())
        print("7.",self.cal_share())
a1=emp("Advik",90000,21,9)
a2=emp("Adarsh",60000,21,5)
a1.display()
print("________________________________")
a2.display()
