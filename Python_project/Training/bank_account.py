class bank:
    account_no = 1
    def __init__(self,name, balance=0):
        
        self.name = name
        self.balance = balance
        self.accountNum = bank.account_no
        bank.account_no = bank.account_no + 1
    
    def __del__(self):
        pass
        
    def get_balance(self,accountNo):
        pass
    
    def withdraw(self,amount):
        if self.balance < amount:
            return -1
    
    def deposit(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()