class Bakery:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
    
    def add_to_inventory(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
    
    def check_inventory(self, item):
        if item in self.inventory:
            return self.inventory[item]
        else:
            return 0

# Note: “Bakery” to initialize the class with Bake and Treats name attribute. “bakery.” to call the expected method, add_to_inventory
# Proof: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables 
# Assertion: https://vegibit.com/python-class-examples/ 
bakery = Bakery('Bake and Treats')
bakery.add_to_inventory('cookies', 8)
print(bakery.check_inventory('cookies'))