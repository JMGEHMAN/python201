"""
## Lab: OO Programming
1. Add a __\_\_`eq`\_\_()__ method to the BankAccount class
  * How you define __\_\_`eq`\_\_()__ is up to you
* Add a __\_\_`mul`\_\_()__ method to the BankAccount class
  * it should create a new BankAccount which does something to the name and multiplies the balance by the second operand
* Add a __\_\_`len`\_\_()__ method to the BankAccount class
* Create a class __`Calculator`__ which acts like a calculator
  * Your class should have methods `add()`, `sub()`, `mult()`, `div()`, `pow()`, and `log()`
  * Each of the above methods (except `log`) should take 1 or 2 arguments
    * for 1 argument, e.g., `add(1)`, your method should add to the running total
    * for 2 arguments, your method should act on those 2 arguments to create a new running total
    * e.g., `add(2, 4)` should produce 6, and then if followed by `multiply(5)`, the result should be 30
* All calculations should be stored, and should be accessible to the caller via the `showcalc()` method (kind of like a printing calculator)
* You should also have an `ac()` "all clear" method which clears the running total and the list of calculations (i.e., showcalc() should produce no output, or "0.0" when preceded by a call to `ac()`)
"""

def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def __repr__(self):
        '''unambiguous representation of the object'''
        return self.__class__.__name__ + '(' + repr(self.name) + ', ' + repr(self.balance) + ')'

    def __str__(self):
        '''string representation of object, for humans
        __repr__ is used if __str__ does not exist'''
        return self.name + ' has ₹' + str(self.balance) + ' in the bank'
   
    def __add__(self, other):
        return self.__class__(self.name + ' + ' + other.name, 
                           self.balance + other.balance - 5.95)



def calculate(operand1, operand2, operator, **kwargs):
    useFloat = False
    
    if kwargs.get('float') == True:
        operand1 = float(operand1)
        operand2 = float(operand2)
        useFloat = True
    else:
        operand1 = int(operand1)
        operand2 = int(operand2)

    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if useFloat:
             return operand1 / operand2
        else:
            return operand1 // operand2
