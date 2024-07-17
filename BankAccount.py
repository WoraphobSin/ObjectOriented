
####################################################################
        
class BankAccount:
    def __init__(self, account_number, account_type, balance, name, password):
        self.__account_number = account_number
        if account_type == 10:
            self.__account_type = "Saving account"
        elif account_type == 20:
            self.__account_type = "Checking account"
        elif account_type == 30:
            self.__account_type = "Brokerage account"
        else:
            self.__account_type = "Saving account"
        if balance >= 0:
            self.__balance = balance
        else: 
            print("Invalid amount!")
        self.__name = name
        self.__password = password

    def deposit(self, amount, password):
        if self.__password != password:
            print("Password is not correct!\n")
        else:
            if amount >= 0:
                self.__balance = self.__balance + amount
                print("Your current balance is " + str(self.get_balance()) + "\n")
            else:
                print("You can't deposit a negative of amount!\n")

    def withdraw(self, amount, password):
        if self.__password != password:
            print("Password is not correct!\n")
        else:
            if (amount > self.__balance) and (amount >= 0):
                print("Your current balance is not enough, Please try again.\n")
            elif amount < 0:
                print("You can't withdraw a negative of amount!\n")
            else:
                self.__balance = self.__balance - amount
                print("Your current balance is " + str(self.get_balance()) + "\n")
                
    def transfer(self, account, amount, password):
        if self.__password != password:
            print("Password is not correct!\n")
        else:
            if (self.__balance >= amount) and (amount >= 0) :
                self.__balance = self.__balance - amount
                account.__balance = account.__balance + amount
                print(f"You transfered {amount} to {account.__account_number}. \n")
            elif amount > self.__balance:
                print("You don't have enough money!\n")
            elif amount < 0:
                print("You can't transfer a negative of amount! \n")
        
    def calInterest(self):
        if self.__account_type == "Saving account":
            interestRate = 1.08
        elif self.__account_type == "Checking account":
            interestRate = 1.02
        elif self.__account_type == "Brokerage account":
            interestRate = 1.15
        else:
            interestRate = 1.00
        print("Your account interest rate is " + str(interestRate) + "\n")

    def _acc_info(self, password):
        if self.__password != password:
            print("Password is not correct! \n")
        else:
            print(f"Account number : " + str(self.get_account_number()) + ", Account type : " + str(self.get_account_type()) +
               ", Account name : " + str(self.get_name()) + ", Balance : " + str(self.get_balance()) +"\n")

    def get_account_number(self):
        return self.__account_number
    
    def get_account_type(self):
        return self.__account_type
    
    def get_balance(self):
        return self.__balance
    
    def get_name(self):
        return self.__name
    
    def get_password(self):
        return self.__password
    
    


