# --- Authentication Decorator for Profile ---
def authenticate(username, password, useremail):
    def decorator(func):
        def wrapper():
            name = input("Enter username: ")
            passd = input("Enter password: ")
            email = input("Enter email: ")
            if username == name and password == passd and email == useremail:
                print("Authentication successful\n")
                return func(name, email)
            else:
                print("Authentication failed\n")
        return wrapper
    return decorator

@authenticate("Bhumika", "bk2006@*", "kadubhumika2468@gmail.com")
def checkprofile(username, email):
    print(f"Administrator of Laptop is {username}")
    print(f"Email: {email}\n")

# --- Account Decorator (Just for Style) ---
def accounts():
    def decorator(func):
        def wrapper():
            print("🔐 Account Privacy")
            return func()
        return wrapper
    return decorator

@accounts()
def accountprivacy():
    print("Bhumika is holder of account. No other user is accessing!\n")

@accounts()
def subscription():
    print("Bhumika is subscribed to the Udemy course!\n")

@accounts()
def projects():
    print("Verified Projects:")
    print("1. FireLock App")
    print("2. Calculator App")
    print("3. Jetpack Compose App\n")

# --- Main Menu ---
def main():
    while True:
        print("---- MENU ----")
        print("1. Check Profile")
        print("2. Account Privacy")
        print("3. Subscription Info")
        print("4. Verified Projects")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            checkprofile()
        elif choice == "2":
            accountprivacy()
        elif choice == "3":
            subscription()
        elif choice == "4":
            projects()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.\n")

# Start Program
main()
