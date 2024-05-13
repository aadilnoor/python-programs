
class Account:
    def __init__(self):
        self.__balance = 0  

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Please enter a valid amount")

    def get_balance(self):
        return self.__balance

acc = Account()
acc.set_balance(1500)
print("The account balance is:", acc.get_balance())