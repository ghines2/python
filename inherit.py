class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def change_password(self, password):
        self.password = password
        print("Your password has been changed to ", self.password)

user1 = User("Graham", "graham.h@teachingstrategies.com", "self.password")
print(user1.password)
user1.change_password("KeptSecretandKeptSafe")


class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0
    
    def Check_Balance(self):
        print(self.name, "has a balance of ", self.balance)
    
bankuser1 = BankUser("Graham", "graham.h@teachingstrategies.com", "self.password")