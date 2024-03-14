#Creating calculator, first time by OOPS.
#Ubaid Ayub
#3/14/2024

#Creating Oject of Calculator
class calculator:
    #Constructor 
    def _init_(self,val1,val2, operator):
        self.val1 = val1
        self.val2 = val2
        self.operator = operator
    #Selectors/Behaviours
    def add(self):
        if self.operator == "+":
            return (self.val1 + self.val2)
    def subtract(self):
        if self.operator == "-":
            return (self.val1 - self.val2)
    def multiple(self):
        if self.operator == "*" or self.operator == "x":
            return (self.val1 * self.val2)
    def divide(self):
        if self.operator == "/":
            return (self.val1/self.val2)


def run_calculator():
    #Creating loop for 4 operators
    for i in range(4):       
        val1 = int(input("enter number 1: "))
        val2 = int(input("enter number 2:"))
        operator = str(input("enter from 4 basic operators:"))
        cal = calculator(val1,val2,operator)
        #Creating Conditions
        if operator =="+":
            print(cal.add())
        elif operator =="-":
            print(cal.subtract())
        elif operator == "*" or operator == "x":
            print(cal.multiple())
        elif operator == "/":
            print(cal.divide())
        else:
            print("please enter from basic operators like (+,-,*,/) only")

#Asking user to quit or not?
def repeat():
    repeat = input("Do you want to exit (Yes/No):")
    if repeat.lower() == "no":
        run_calculator()
    else:
        print("you have closed the calcultor! Successfully")
        
#Calling Functions
run_calculator()
repeat()
