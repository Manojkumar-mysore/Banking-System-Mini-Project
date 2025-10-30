
class Account_class:

    def __init__(self,id,holder_name):
        self.id = id
        self.holder = holder_name
        self._balance = 0   # encapsulation (protected)

    def check_balance(self):
        print(f"your balance is :{self._balance} \n")

    def deposit(self):
        deposit_amount = int(input("enter the deposit amount : "))

        self._balance += deposit_amount
        print(f"deposit successful. updated balance :{self._balance} \n")

    def withdraw(self,withdraw_amount):

        if self._balance >= withdraw_amount:
            self._balance -= withdraw_amount
            print(f"withdraw successful. updated balance :{self._balance} \n")
        else:
            print("balance is less than ask or insufficient balance \n")


class Savings_account(Account_class):  # inheritance (inheriting class account)

    def calculate_interest(self):
        interest_rate = 0.04  # 4%
        interest = self._balance * interest_rate
        print(f" interest : {interest} \n")

class Current_account(Account_class):

    def withdraw(self,withdraw_amount): # polymorphism
        overdraft_limit = 1000
        if withdraw_amount <= self._balance + overdraft_limit:
            self._balance -= withdraw_amount
            print(f"withdraw successful. updated balance :{self._balance} \n")
        else:
            print("withdrawal is over limit \n")

class Bank:

    def __init__(self, name ,city ):
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self):
        try:
            holder_name = input("enter the holder name : ")
            account_type = input("enter the account type savings /current : ").lower()
            id = int(input("enter the id : "))

            if id in self.__accounts:
                print("account id is already exists ! \n")
                return

            if account_type == "savings" :
                new_account = Savings_account(id ,holder_name)   # objects by using this we inherit Account class

            elif account_type == "current":
                new_account = Current_account(id ,holder_name)      # objects by using this we inherit Account class

            self.__accounts[id] = new_account
            print(f"account created successful. for {holder_name} with id {id} \n")
            print(self.__accounts)

        except ValueError:
            print("invalid input, check id or account type \n")


    def get_account(self):
        # return self.__accounts.get(account_id,None)
        account_id = int(input("enter the account id : "))

        if account_id not in self.__accounts:
            print("account not found \n")
        else:
            account = self.__accounts[account_id]
            print(f" \n id : {account.id} \n holder name : {account.holder} \n")
            return self.__accounts[account_id]

    def menu(self):

        while True:
            try:
                print("------wellcome to bank-------")
                print("1.create account")
                print("2.select account")
                print("3.to exit")

                choice = int(input("choose the option 1/2/3 : "))

                if choice == 1:
                    self.create_account()

                elif choice == 2:
                    account = self.get_account()
                    if account :
                        self.account_menu(account)

                elif choice == 3:
                    print("thankyou for visiting our bank ")
                    break
                else:
                    print("invalid input, please choose correct options \n")
            except ValueError:
                print("invalid input, please try again \n")

    def account_menu(self,account):
        while True:
            try:
                print(f"----account menu ({account.holder})")
                print("1.check balance")
                print("2.deposit money")
                print("3.withdraw money")
                if isinstance(account,Savings_account):
                    print("4.calculate interest")
                print("5.back to menu")

                choice = int(input("choose the menu option 1/ 2/ 3/ 4 :"))

                if choice == 1:
                        account.check_balance()

                elif choice == 2:
                        account.deposit()

                elif choice == 3:
                       amount = int(input("enter the withdraw amount :"))
                       account.withdraw(amount)

                elif choice == 4:
                        account.calculate_interest()
                elif choice == 5:
                    print("")
                    break
                else:
                    print("invalid input, please choose correct numbers \n")

            except ValueError:
                print("invalid input, please try again \n")


# run program
def main():
    my_bank = Bank("manoj bank of india","mysuru")
    my_bank.menu()

if __name__=="__main__":
    main()

