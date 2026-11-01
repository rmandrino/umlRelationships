from abc import ABC, abstractmethod

# Interface
class Payable(ABC):
    @abstractmethod
    def pay(self):
        pass


# Implementing class
class Payment(Payable):
    def pay(self):
        print("Payment completed")


# Main program
payment = Payment()
payment.pay()