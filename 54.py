'''Data Encapsulation:Encapsulating data using a method
1 we have to design base class information for scenario based programs
2 design logic for main part
3 design second class (action class)
'''
from datetime import datetime
class Bus:
    def __init__(self,bno,ac,cap):
        self.bno = bno
        self.ac = ac
        self.cap = cap
    def get_bno(self):
        return self.bno
    def get_ac(self):
        return self.ac
    def get_cap(self):
        return self.cap
    def display(self):
        print(f"1.{'BUS NO':<10}",self.get_bno())
        print(f"2.{'AC':<10}",self.get_ac())
        print(f"3.{'BUS CAPACITY':<10}",self.get_cap())
class Booking:
    def __init__(self):
        name=input("Enter passenger name: ")
        bno=int(input("Enter bus no: "))
        d=input("Enter booking date (dd-mm-yyyy): ")
        date=datetime.strptime(d,"%d-%m-%Y").date()
        self.name = name
        self.bno = bno
        self.date = date
    def make_booking(self,BUSES,BOOKINGS):
        if(self.is_availabale(BUSES,BOOKINGS,self.bno,self.date)):
            BOOKINGS.append(self)
        else:
            print("Bus is full")
    def is_availabale(self,BUSES,BOOKINGS,bno,date):
        booked=0
        capacity=0
        for i in BUSES:
            if(i.bno==bno):
                capacity=i.cap
        for i in BOOKINGS:
            if(i.bno==bno and i.date==date):
                booked=booked+1
        return booked<capacity
    def  display_book_info(self):
        print("Name: ",self.name)
        print("Bus no: ",self.bno)
        print("Booking date: ",self.date)
BUSES=[Bus(1,True,2),Bus(2,False,60),Bus(3,True,55)]
for i in BUSES:
    i.display()
    print("------------------------------")
BOOKINGS=[]
while True:
    print("PRESS 1 - TO BOOK TICKET")
    print("PRESS 2 - TO VIEW BOOKINGS")
    print("PRESS 3 - TO EXIT")
    ch=int(input("Enter your choice:"))
    if ch==1:
        b=Booking()
        b.make_booking(BUSES,BOOKINGS)
    elif(ch==2):
        if not BOOKINGS:
            print("No bookings yet")
        else:
            for i in BOOKINGS:
                i.display_book_info()
    elif ch==3:
        print("Exiting the system, Thank you")
        break
    else:
        print("Invalid choice")




