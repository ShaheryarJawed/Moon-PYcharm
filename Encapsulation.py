class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account-number
        self.balance = balance

        def deposit(self,amount):
            self.balance += amount

            def withdraw(self,amount):
                if amount <= self.balance:
                    self.balance -= amount
                else:
                    print ("Insufficient Balance")

                    def get_balance(self):
                        return self.__balance

                    account1 = BankAccount("12345", 5000)
                    account1.deposit(1000)
                    account1.withdraw(2000)
                    print(account1.get_balance())


