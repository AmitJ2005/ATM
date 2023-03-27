class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
                
    def check_pin(self):
        Amit = input("Enter the Pin for   ")
        if Amit == self.pin:
            return True
        else:
            print("Invalid pin   ** Tu kaya kar raha hai Bhai  **")
            return False

    def menu(self):
        user_input = input('''
        1 : create pin 
        2 : deposit amount
        3 : Withdraw amount  
        4 : Check balance 
        5 : exit
         ''')

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.exit()
        else:
            print("Andha hai kaya !!..\n"
                  "4 Option Diya Hai Phir Bhi : Dimag Laga Raha Hai")

    def create_pin(self):
        self.pin = input("create your pin :- ")
        if len(str(self.pin))<=4:
            print("Pin Set Successfully ")
        else:
            print("Pin not more then 4 digits")
            self.create_pin()
        self.menu()

    def deposit(self):
        if  self.check_pin():
            amount = int(input("Enter The Amount for deposit :-  "))
            self.balance = self.balance + amount
            print("Deposit successful")
        self.menu()

    def withdraw(self):
        if self.check_pin():
            amount = int(input("Enter Withdraw Amount for Withdraw:- "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("WithDraw Successful")
            else:
                print("Insuf balance ")
        self.menu()

    def check_balance(self):
        if self.check_pin():
            print("your remaninig balance is : {}".format(self.balance))
        self.menu()

    def exit(self):
        print("Aap Sai Mil Kar Kushi Hui ")


sbi=Atm()

