# Order class
class Order:
    def display(self):
        print("Order placed")


# Customer class
class Customer:
    def __init__(self, order):
        self.order = order

    def place_order(self):
        self.order.display()


# Main program
order = Order()
customer = Customer(order)

customer.place_order()