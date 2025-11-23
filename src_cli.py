# cli.py
from encryption import encrypt, decrypt
from generator import generate_random_password
from storage import password_store, set_master_password, verify_master_password

def add_password():
    print("\n== Add Password ==")
    account = input("Enter account name (e.g., Gmail): ")
    choice=input("Do you want to generate a random password? (y/n): ").lower()
    if(choice == 'y'):
        pwd = generate_random_password()
        # preserved original "print" shape (note: original used a set-literal in print)
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
        try:
            choice=int(input("Enter choice: "))
        except:
            print("Invalid choice.")
            continue
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