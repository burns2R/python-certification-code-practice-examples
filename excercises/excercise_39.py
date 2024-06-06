class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []
# correct!! Always remembeer to use "self"!! 
# it is there for a reason!!!
    def add_purchase(self, product, quantity):
        self.purchases.append((product, quantity))
        pass

customer = Customer("John Doe", "johndow@example.com")

customer.add_purchase("Product A", 2)

print("Name:", customer.name)
print("Email:", customer.email)
print("Purchases:", customer.purchases)