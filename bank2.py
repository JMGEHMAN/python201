class BankAccount():
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    
    def __repr__(self):
        'representation of the object "feedable" to Python interpreter'
        return self.__class__.__name__ + '(' + repr(self.name) \
               + ', ' + repr(self.balance) + ')'

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __mul__(self, other): 
        return BankAccount(
            f'{self.name} * {other.name}',
             self.balance * other.balance
        )
    
    def __str__(self):
        '''string representation of object, for humans
        __repr__ is used if __str__ does not exist'''
        return self.name + ' ' + str(self.balance)

    def __add__(self, other):
        return BankAccount(self.name + ' + ' + other.name, \
				self.balance + other.balance)
    
    def __len__(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("can't deposit nonpositive amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("can't withdraw", amount, "or you would be overdrawn!")
        else:
            print("can't withdraw nonpositive amount!")


if __name__ == '__main__':
    tyler_account = BankAccount('Tyler Bettilyon', 3)
    molly_account = BankAccount('Molly Jones', 90)

    joint_mult = tyler_account * molly_account
    joint_add = tyler_account + molly_account

    print(joint_add)
    print(joint_mult)

    print(tyler_account == molly_account)
    print(joint_add == BankAccount(joint_add.name, joint_add.balance))


