import random
import string

encryption_dict={'a':'@','b':'#','c':'$','d':'%','e':'&','f':'*','g':'+','h':'!','i':'?','j':'^','k':'~','l':'-','m':'=','n':'<','o':'>','p':'/','q':'[','r':']','s':'{','t':'}','u':'|','v':':','w':';','x':'"','y':',','z':'.'}

decryption_dict = {}
for key, value in encryption_dict.items():
    decryption_dict[value] = key

password_store={}

master_password=None

def encrypt(text):
    text = text.lower()
    encrypted_text = ""
    for char in text:
        if char in encryption_dict:
            encrypted_text += encryption_dict[char]
        else:
            encrypted_text += char  
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    for char in text:
        if char in decryption_dict:
            decrypted_text += decryption_dict[char]
        else:
            decrypted_text += char  
    return decrypted_text

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

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

def add_password():
    print("\n== Add Password ==")
    account = input("Enter account name (e.g., Gmail): ")
    choice=input("Do you want to generate a random password? (y/n): ").lower()
    if(choice == 'y'):
        pwd = generate_random_password()
        print(f"Generated password: ", {pwd})
    else:
        pwd=input("Enter password to save: ")
    encrypted_pwd=encrypt(pwd)
    password_store[account]=encrypted_pwd
    print(f"Password saved for {account}. Encrypted version: {encrypted_pwd}")

def retrieve_password():
    print("\n== Retrieve Password ==")
    account=input("Enter account name: ")
    if account in password_store:
        encrypted_pwd = password_store[account]
        print("Encrypted password: ",{encrypted_pwd})
        choice=input("Do you want to Decrypt (y/n): ").lower()
        if choice=='y':
            print("Decrypted password: ",decrypt(encrypted_pwd))
        else:
            print("Decryption skipped.")
    else:
        print("No password found for this account.")

def main():
    print("Welcome to the Password Manager System\n")
    set_master_password()
    while True:
        print("\nMenu:")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice=int(input("Enter choice: "))
        if(choice==1):
            if(verify_master_password()):
                add_password()
        elif(choice==2):
            if(verify_master_password()):
                retrieve_password()
        elif(choice==3):
            print("Thank You")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()