class PaymentMethod:

    """
    Base class with a common interface method.
    All child classes must implement make_payment().
    """
    def make_payment(self):
        raise NotImplementedError("Subclass must be implemented this method")
    

class CreditCard(PaymentMethod):

    def make_payment(self, amount):
        process_fee = amount * 0.02
        total = amount + process_fee
        return f"Credit Card Payment Successful. Amount is {total}"
    

class DebitCard(PaymentMethod):

    def make_payment(self, amount):
        process_fee = amount * 0.01
        total = amount + process_fee
        return f"Debit Card Payment Successful. Amount is {total}"
    


class UPIPayment(PaymentMethod):

    def make_payment(self, amount):
        process_fee = 10
        total = amount + process_fee
        return f"UPI Payment Successful. Amount is {total}"
        

def process_payment(payment_method:PaymentMethod,amount):
    print(payment_method.make_payment(amount))


payment_list = [
    CreditCard(),
    DebitCard(),
    UPIPayment()
]

for method in payment_list:
    process_payment(method,1000)