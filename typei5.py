class Ecommerce:
    def __init__(self, info):
        self.name = info[0]
        self.type_user = info[1]
        self.address = info[2]
        self.phone_no = info[3]
        self.email = info[4]

class Authentication(Ecommerce):
    def authenticate(self):
        user = input("Are you visiting our website for the first time? (yes/no): ").strip().lower()
        if user == "yes":
            self.registration()
        else:
            self.login()

    def registration(self):
        print(f"{self.name}, please complete the registration first, then you can log in.")

    def login(self):
        print(f"{self.name}, you can proceed to log in.")

class Dashboard(Authentication):
    def user_dashboard(self):
        print(f"Welcome {self.name} to the user dashboard! Enjoy shopping with Electrocart.")

class SuperUser(Ecommerce):
    def superuser_dashboard(self):
        print(f"{self.name}, you are a superuser. Please log in to access the superuser dashboard.")


print("Welcome to Electrocart! Get the best deals on electronic gadgets.")
name = input("Enter your name: ")
type_user = input("Enter your user type (normal/super): ")
address = input("Enter your address: ")
phone_no = input("Enter your phone number: ")
email = input("Enter your email address: ")

info = [name, type_user, address, phone_no, email]

if type_user == "normal":
    print("You are a normal user.")
    obj = Dashboard(info)
    obj.authenticate() 
    obj.user_dashboard() 
elif type_user == "super":
    print("You are a superuser.")
    obj = SuperUser(info)
    obj.superuser_dashboard()  
else:
    print("Invalid user type. Please restart and choose either 'normal' or 'super'.")
