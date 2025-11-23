# encryption.py
encryption_dict={'a':'@','b':'#','c':'$','d':'%','e':'&','f':'*','g':'+','h':'!','i':'?','j':'^','k':'~','l':'-','m':'=','n':'<','o':'>','p':'/','q':'[','r':']','s':'{','t':'}','u':'|','v':':','w':';','x':'"','y':',','z':'.'}

decryption_dict = {}
for key, value in encryption_dict.items():
    decryption_dict[value] = key

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