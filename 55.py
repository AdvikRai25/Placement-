'''method overloading same method name different arguments or number of arguments
method overriding same method name same arguments while inheritance
It is used to call superclass methods, and to access the superclass constructor.
'''
class vehicle:
    def __init__(self, brand, fuel_type):  # Corrected __init__
        self.brand = brand
        self.fuel_type = fuel_type

    def display_info(self):
        print("Brand      : ", self.brand)
        print("Fuel Type  : ", self.fuel_type)

class car(vehicle):
    def __init__(self, brand, fuel_type, model):  
        super().__init__(brand, fuel_type)
        self.model = model

    def display_details(self):
        self.display_info()
        print("Model      : ", self.model)

c = car("Toyota", "Petrol", "Innova")
c.display_details()
