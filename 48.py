''' one variable common for all object is called class varaible
instance variable that belongs to an object (instance) of a class.
global variable declared outside of all functions and classes.
local variable declared inside a function.Only accessible within that function

name (parameter)	Local Variable
self.name	        Instance Variable
a1, a2	            Global Variables
'''
class LC37:
    def student(self,name):
        self.name = name
    def display(self):
        print("The name is",format(self.name))
a1 = LC37()
a2 = LC37()
a1.student("advik")
a2.student("deon")
a1.display()
a2.display()
