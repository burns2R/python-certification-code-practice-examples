class CustomerPurchaseData:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.purchase_amount_history = []

    def add_purchase(self, amount):
        self.purchase_amount_history.append(amount)

    def get_total_purchase(self):
        return sum(self.purchase_amount_history)
    
customer1 = CustomerPurchaseData("A101")
customer1.add_purchase(100)
customer1.add_purchase(200)
# Correct!! Remeber get_total_purchase(self) is a method
# that takes no arguments, so remember the '()'!!
print("Total purchase: ", customer1.get_total_purchase())