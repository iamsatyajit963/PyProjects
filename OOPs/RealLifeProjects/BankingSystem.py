"""
                SIMULATE A BANKING SYSTEM
    - Give a prompt to the user asking if they wish to create a new Savings Account or access an existing one.
    - If the user would like to crea a new account, accept their name and initial deposit, and create a 5digit
    random number and make it as the acount number of their new Savings Account.
    - If they are accessing an existing account, accept their name and account number to validate the user, 
    and give them options to withdraw, deposit or display their available balance.
"""
from abc import ABCMeta, abstractclassmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractclassmethod
    def createAccount():
        return 0
    
    @abstractclassmethod
    def authenticate():
        return 0
    
    @abstractclassmethod
    def withdraw():
        return 0
    
    @abstractclassmethod
    def deposit():
        return 0
    
    @abstractclassmethod
    def displayBalance():
        return 0
    
class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self,name,initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]  
        print("Account creation successful. Your A/C no -> ", self.accountNumber)      
    
    def authenticate(self, name, accountNumber):
        print(self.savingsAccounts)
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("Authentication has been successful...")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed...")
                return False
        else:
            print("Account Not present")
            return False
    
    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("You cannot withdraw more than the available balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal is successful.")
            self.displayBalance()
            
    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] += depositAmount
        print("Deposit successful.")
        self.displayBalance()
    
    def displayBalance(self):
        print("Available balance is -> {}".format(self.savingsAccounts[self.accountNumber][1]))\
            
         
savingsAccounts = SavingsAccount()
while True:
    print(" Enter 1 to create a new account")
    print(" Enter 2  to access an existing account")
    print(" Enter 3 to exit")

    userChoice = int(input())
    
    if (userChoice == 1):
        name = input("Enter you name: ")
        print(type(name))
        initialDeposit = int(input("Enter the amount you want to deposit: "))
        savingsAccounts.createAccount(name, initialDeposit)
    elif(userChoice == 2):
        name = input("Enter you name: ")
        accountNumber = input("Enter the account Number: ")
        if (savingsAccounts.authenticate(name,accountNumber)):
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to previous menu")
                userChoice = int(input())
                if userChoice == 1:
                    withdrawalAmount = int(input("Enter the amount you want to withdraw: "))
                    savingsAccounts.withdraw(withdrawalAmount)
                elif userChoice == 2:
                    depositAmount = int(input("Enter the amount you want to deposit: "))
                    savingsAccounts.deposit(depositAmount)
                elif userChoice == 3:
                    savingsAccounts.displayBalance()
                elif userChoice == 4:
                    break
                else:
                    print("Invalid choice.")
    elif userChoice == 3:
        quit()