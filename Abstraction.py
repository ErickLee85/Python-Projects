from abc import ABC, abstractmethod
class Target(ABC):
    def paySlip(self, amount):
        print("Your total purchase amount is: ${}.".format(amount))

    @abstractmethod
    def payment(self, amount):
        pass

class giftCardPayment(Target):
 
    def payment(self,amount,giftCard):        
        if giftCard < amount:
            print("Insufficient funds, please try another payment method.")
        else:
            giftCard = giftCard - amount
            print("Your purchase amount of ${} has been paid with a gift card, your remaining balance is: ${}.".format(amount,giftCard))


obj1 = giftCardPayment()
obj1.paySlip(199)
obj1.payment(199,200)


