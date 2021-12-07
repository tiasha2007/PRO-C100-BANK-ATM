class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin=pin
        self.Account=account

    def check_balance(self):
        print("Your balance is:-")
        print("Muthooth=100")
        print("SBI=200")
        print("Pnb=300")

    def withdrawl1(self,muthooth):
        new_amount=100 - muthooth
        print("You have withdrawn amount"+str(muthooth)+".Your remaining balance is "+ str(new_amount))

    def withdrawl2(self, sbi):
        new_amount = 200 - sbi
        print("You have withdrawn amount "+str(sbi) + ". Your remaining balance is "+ str(new_amount))

    def withdrawl3(self,pnb):
        new_amount = 300 - pnb
        print("You have withdrawn amount "+str(pnb) + ". Your remaining balance is "+ str(new_amount))
    
    def main():
        print("Welcome to Punjab National Bank! The wizards and witchs bank")
        Account = input("Please enter your account pin or number: ")
        Card_number = input("Insert your key number:- ")
        pin_number  = input("Enter your pin number:- ")

        new_user =  Atm(Account,Card_number,pin_number)

        print("Choose your activity ")
        print("1.Balance Enquriy   2.Withdrawl")
        activity = int(input("Enter activity number :- "))

        if (activity == 1):
            new_user.check_balance()
        elif (activity == 2):
            print("1. Add Muthooth")
            print("2. Add Sbi")
            print("3. Add Pnb")
            choose = int(input("1. Add Muthooth  2. Add Sbi 3. Add Pnb: "))
        if (choose == 1):
           muthooth = int(input("Enter the amount:- "))
           new_user.withdrawl1(muthooth)
        if (choose == 2):
           sbi = int(input("Enter the amount:- "))
           new_user.withdrawl2(sbi)    
        if (choose == 3):
           pnb = int(input("Enter the amount:- "))
           new_user.withdrawl3(pnb)
        else:
            print("Enter a valid number")

    if __name__ == "__main__":
            main()