# Note: Answer should be the two in quotes “__init__”(...) and “self”
# Proof: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables 
# Assertion: https://vegibit.com/python-class-examples/ 
class Snack:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def add_items(self, quantity):
        self.quantity += quantity
        print(f'{quantity} {self.name}(s) added to inventory. Total quantity now: {self.quantity}')

wafers = Snack('wafer', 2.1, 10)
popcorn = Snack('popcorn', 1.5, 8)

wafers.add_items(10)
popcorn.add_items(5)