class bank:
    def __init__(self):
        balance = 0
        name = ""
        sex = ""
        birth = ""
        address = ""
        work = ""
    
    def initial(self,initial):
        bank.balance = initial
    def deposit(self,bal):
        bank.balance = bank.balance + bal
    def withdraw(self,wid):
        bank.balance = bank.balance - wid
    def name(self, name):
        bank.name = name
    def sex(self, sex):
        bank.sex =sex
    def birth(self, birth):
        bank.birth = birth
    def address(self, address):
        bank.address = address
    def work(self, work):
        bank.work = work
        
class bankingsystem(bank):
    
            
    def createBA():
        bank1 = bank()                      
        print("Create Bank Account\n")
        print("Add Account\n")
        a = input("Full Name:") 
        bank1.name(a)
        b = input("Sex:")
        bank1.sex(b)
        c = input("Date of Birth:")
        bank1.birth(c)
        d = input("Address:")
        bank1.address(d)
        e = input("Work/Profession:")
        bank1.work(e)
        
        
        try:
            ini = float(input("initial deposit:"))
            
        except ValueError:
            print("No initial Deposit!")
            return None
        if(ini !=0):
            bank1.initial(ini)
        else:
            print("Not accepted!")
        #goto select
            
    
    def manage():
        bank1 = bank()
        print("[1] Deposit\n")
        print("[2] Withdraw\n")
        print("[3] Balance Inquery\n")
        print("[4] Account Information\n")
        choice2 = int(input("Choice: "))
        if choice2 == 1:
            bal1 = float(input("deposit amount:"))
            bank1.deposit(bal1)
            #bank1.balance = bank1.balance+bal
            #goto select
        elif choice2 ==2:
            bal = float(input("withdraw amount:"))
            bank1.withdraw(bal)
            #bank1.withdraw = bank1.withdraw+bal
            #goto select
        elif choice2 ==3:
            print("Balance: " ,bank1.balance)
            #goto select
        elif choice2 ==4:
            print("Full Name: " ,bank1.name)
            print("Sex: " ,bank1.sex)
            print("Date of Birth: " ,bank1.birth)
            print("Address: " ,bank1.address)
            print("Work/profession: " ,bank1.work)
            
            #goto select
                
        else:
            print("wrong input")
            #goto select
    def main():
        
        print("\n\nBank Accout\n\n\n")
        print("[1] Create Bank Account\n")
        print("[2] Manage Bank Account\n")
        
    while(1):
        main()
        choice = int(input("Choice: "))
        if choice == 1:
            createBA()
        else:
            manage()
        

