class BankAccount:

    """
        Encapsulation Example:
        - balance is private (__balance)
        - Access only through getter & setter methods
    """
    def __init__(self,bank_name,bankcode,balance):
        self.bank_name = bank_name
        self._bankcode = bankcode # Protected
        self.__balance = balance # Private

    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("balance is not negative")
        self.__balance += amount

    def withdrawn(self,amount):
        if amount <= 0:
            raise ValueError("withdrawn amount must be greater than zero")
        self.__balance -= amount


bank = BankAccount("ICICI","IFSC",60000)
bankcode = bank._bankcode
balance = bank.get_balance()

print(f"{bank.bank_name} Bank have remaining balance is {balance}")