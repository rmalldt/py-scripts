from datetime import datetime, timezone


class Account:
    """Simple account class with balance"""

    # Fields and methods starting with _ are meant for internal use only
    # similar to private fields and methods even though it is NOT Strictly
    # enforced by Python.
    @staticmethod
    def _current_time():
        utc_time = datetime.now(tz=timezone.utc)
        return utc_time.astimezone()  # localize time

    def __init__(self, name, balance):
        self._name = name  # internal field

        # Python performs name mangling for fields starting with dunder
        # by prefixing Class name to the method name.
        # In this case, __balance will be converted to _Account__balance
        # So, when we use the field inside the class it refers to correct field name.
        # But when this field is referred outside the class, the correct fiels name is hidden.
        # This is done to prevent accident change of the fields from outside the class.
        self.__balance = balance

        self._transaction_list = [(Account._current_time(), balance)]  # internal field
        print(f"Account created for {self._name}")

    # ------------------ Public Methods
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero or less than your balance")

    def show_balance(self):
        print(f"Balance is {self.__balance}")

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                transaction_type = "deposited"
            else:
                transaction_type = "withdrawn"
            print(f"{amount:6} was {transaction_type} on {date}")


# ------------------ Test

if __name__ == "__main__":
    jim = Account("Jim", 2000)
    jim.show_balance()
    jim.deposit(1000)
    jim.show_balance()
    jim.withdraw(500)
    jim.show_balance()
    jim.show_transactions()

    jim.__balance = 0
    jim.show_balance()

    print(jim.__dict__)
