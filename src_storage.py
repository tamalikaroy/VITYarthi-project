# storage.py
password_store = {}
master_password = None

def set_master_password():
    global master_password
    while True:
        pwd1=input("Set master password: ")
        pwd2=input("Confirm master password: ")
        if(pwd1==pwd2): 
            master_password = pwd1
            print("Master password set successfully!")
            break
        else:
            print("Passwords don't match or are empty. Try again.")

def verify_master_password():
    while True:
        pwd=input("Enter your master password: ")
        if pwd==master_password:
            return True
        else:
            print("Incorrect master password. Try again.")