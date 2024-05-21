import hashlib

class User:
    def __init__(self, name, password, initial_deposit):
        self.name = name
        self.hashed_password = self.hash_password(password)
        self.account = Account(initial_deposit)

    def get_name(self):
        return self.name

    def get_account(self):
        return self.account

    def verify_password(self, password):
        return self.hashed_password == self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


class Account:
    def __init__(self, initial_deposit):
        self.balance = initial_deposit

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False


class Bank:
    def __init__(self):
        self.users = {}

    def create_user(self, name, password, initial_deposit):
        if name not in self.users:
            self.users[name] = User(name, password, initial_deposit)
            print(f"User {name} created with initial deposit of {initial_deposit}")
        else:
            print(f"User {name} already exists.")

    def get_user(self, name):
        return self.users.get(name)

    def deposit(self, name, amount):
        user = self.get_user(name)
        if user:
            user.get_account().deposit(amount)
            print(f"Deposited {amount} to {name}'s account. New balance: {user.get_account().get_balance()}")
        else:
            print(f"User {name} not found.")

    def transfer(self, from_user, to_user, amount):
        user_from = self.get_user(from_user)
        user_to = self.get_user(to_user)

        if user_from and user_to:
            if user_from.get_account().withdraw(amount):
                user_to.get_account().deposit(amount)
                print(f"Transferred {amount} from {from_user} to {to_user}")
                print(f"{from_user}'s new balance: {user_from.get_account().get_balance()}")
                print(f"{to_user}'s new balance: {user_to.get_account().get_balance()}")
            else:
                print(f"Transfer failed. Insufficient funds in {from_user}'s account.")
        else:
            print("One or both users not found.")


def main():
    bank = Bank()

    while True:
        print("\nWelcome to the Bank")
        print("1. Create new account")
        print("2. Login to existing account")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            create_new_account(bank)
        elif choice == '2':
            login_to_account(bank)
        elif choice == '3':
            print("Thank you for using the Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def create_new_account(bank):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    initial_deposit = float(input("Enter initial deposit: "))
    bank.create_user(name, password, initial_deposit)


def login_to_account(bank):
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    user = bank.get_user(name)

    if user and user.verify_password(password):
        while True:
            print(f"\nHello, {user.get_name()}")
            print("1. Deposit money")
            print("2. Transfer money")
            print("3. Check balance")
            print("4. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                deposit_money(bank, user)
            elif choice == '2':
                transfer_money(bank, user)
            elif choice == '3':
                check_balance(user)
            elif choice == '4':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password. Please try again.")


def deposit_money(bank, user):
    amount = float(input("Enter amount to deposit: "))
    bank.deposit(user.get_name(), amount)


def transfer_money(bank, from_user):
    to_user = input("Enter recipient's name: ")
    amount = float(input("Enter amount to transfer: "))
    bank.transfer(from_user.get_name(), to_user, amount)


def check_balance(user):
    print(f"Your current balance is: {user.get_account().get_balance()}")


if __name__ == "__main__":
    main()
