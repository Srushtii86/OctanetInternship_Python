class ATM:
    def __init__ (self, UserId , Pin , Balance=0):
        self.UserId = UserId
        self.Pin = Pin
        self.Balance = Balance
        self.Transaction =[]
    
    def DisplayBalance(self):
        print(f"Your Balance is {self.Balance}")
    
    def DisplayTransaction(self):
        print(f"Transactions of ID {self.UserId} :")
        for transaction in self.Transaction:
            print(transaction)
        self.DisplayBalance()
    
    def Deposit(self,amt):
        if (amt>0) :
            self.Balance += amt
            self.Transaction.append(f"Deposit : {amt}")
            print(f"Amount successfully deposited and the Balance is {self.Balance}" )
        else:
            print("Invalid amount ")
    
    def Withdraw(self,amt):
        if (amt>0 and amt<self.Balance) :
            self.Balance -= amt
            self.Transaction.append(f"Withdrawn : {amt}")
            print(f"Amount successfully withdrawn and the Balance is {self.Balance} " )
        else:
            print("Invalid amount or Insufficient Bank Balance!")
    
    def Transfer(self,receiver,amt):
        if(self.Balance >= amt and amt > 0 ):
            self.Balance -= amt
            self.Transaction.append(f"Transfer to  UserId {receiver.UserId} : {amt}")
            receiver.Balance += amt
            receiver.Transaction.append(f"Transfer from UserId {self.UserId} : {amt}")            
            print("Transfer Successful.")
    
    
def main():
    user1 = ATM(1,1234,1000)
    user2 = ATM(2,4567,2000)
    # user1.DisplayBalance()
    # user1.Deposit(2000)
    # user1.Transfer(user2,500)
    # user1.DisplayTransaction()
    # user2.DisplayTransaction()
    user = None
    while not user:
        id = input("Enter User ID: ")
        pin = input("Enter User PIN: ")
        id = int(id)
        pin = int(pin)
        if(id == user1.UserId and pin == user1.Pin):
            user = user1
        elif(id == user2.UserId and pin == user2.Pin):
            user = user2
        else:
            print("Invalid UserId or Pin")
            
    while True:
        print("\nWelcome User")
        print("1. Deposit ")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Transactions History")
        print("5. Quit")
        choice = int(input("Enter Any One of the options"))
        
        if(choice == 1):
            amt = float(input("Enter amount to be Deposited:"))
            user.Deposit(amt)
        
        elif(choice == 2):
            amt = float(input("Enter amount to be Withdrawn:"))
            user.Withdraw(amt)
        
        elif(choice == 3):
            receiverId = int(input("Enter Recipients User Id: "))
            if(receiverId == user1.UserId):
                receiver = user1
            elif(receiverId == user2.UserId):
                receiver = user2
            else:
                print("Invalid user Id of receiver")
                break
            amt = float(input("Enter the amount to be transferred: "))
            user.Transfer(receiver,amt)
        
        elif(choice == 4):
            user.DisplayTransaction()
        
        elif(choice == 5):
            print("Exiting ATM. Thank you!")
            break
            
        else:
            print("Enter a Valid choice from 1 to 5")
        
if __name__ == "__main__" :
    main()