import pwinput

# simple signup/login system 
dic = {}
class signup:
    def __init__(self, user, passw):
        self.user = user
        self.passw = passw
    
    def store(self):
        dic[self.user] = self.passw
    

class login(signup):
    
    def details(self):
        print("Write You User name and password to check: --")
        
        user = input("Enter Username: ")
        passw = pwinput.pwinput("Enter password: ")
        
        if user in dic:
            if dic[user] == passw:
                print("Succesfully authenticated")
            else:
                print("Not authenticated")
        else:
            print("Not authenticated")

users = int(input("How many users?: "))

for i in range(users):
    usnam = input("Enter user name for " + str(i+1)+ " user: ")
    passw = pwinput.pwinput("Enter password for " + str(i+1)+ " user: ")
    obj = login(usnam, passw)
    obj.store()

obj.details()
    