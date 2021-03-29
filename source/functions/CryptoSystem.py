from cryptography.fernet import Fernet
from Option import Option
class CryptoSystem:
    
    def Crypto_system_options():
        optionList = []
        optionList.append(Option(1, "generate the key"))
        optionList.append(Option(2, "encrypt the message"))
        optionList.append(Option(3, "decrypt the message"))
        optionList.append(Option(4, "encrypt the file"))
        optionList.append(Option(5, "decrypt the file"))
        optionList.append(Option(6, "back to main menu"))

        for option in optionList:
            print("[", option.number, "] ", option.descritpion)
        selection = input("請輸入需要的功能：").strip()
        if(selection=="1"):
            Key_generate.write_key()
        elif(selection=="2"):
            Encrypt.encrypt_message()
        elif(selection=="3"):
            Decrypt.decrypt_message()
        elif(selection=="4"):
            Encrypt.encrypt_file()
        elif(selection=="5"):
            Decrypt.decrypt_file()
        elif(selection=="6"):
            return 
    


class Decrypt:

    def decrypt_message():
        try:
            key=open("key.key", "rb").read()
            encrypted=input("enter the cipher : ").encode()
            if encrypted==b'':
                print("Please enter the cipher")
                return 0
            f = Fernet(key)
            
            decrypted_encrypted = f.decrypt(encrypted)
            print(decrypted_encrypted)

        except FileNotFoundError:
            print("Please use [ 3 ] to generate the key first")
            return 0
        

    def decrypt_file():
        try:
            key=open("key.key", "rb").read()
        except FileNotFoundError:
            print("Please use [ 3 ] to generate the key first")
            return 0
        f = Fernet(key)
        try:
            encrypted_file_path=input("Enter the path of encryped file;example : test_file\n").encode()
            with open(encrypted_file_path, "rb") as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(encrypted_file_path, "wb") as file:
                file.write(decrypted_data)
        except FileNotFoundError:
            print("Please enter the correct file path")
            return 0

class Encrypt:

    def encrypt_message():
        try:
            key=open("key.key", "rb").read()
        except FileNotFoundError:
            print("Please use [ 3 ] to generate the key first")
            return 0
        f = Fernet(key)
        message = input("enter message").encode()
        encrypted = f.encrypt(message)
        print(encrypted)
    
    def encrypt_file():
        try:
            key=open("key.key", "rb").read()
        except FileNotFoundError:
            print("Please use [ 3 ] to generate the key first")
            return 0
        file_path=input("Enter the path of file;example : test_file\n")
        try:
            with open(file_path, "rb") as file:
                file_data = file.read()
            f = Fernet(key)
            encrypted_data = f.encrypt(file_data)
            with open(file_path, "wb") as file:
                file.write(encrypted_data)
        except FileNotFoundError:
            print("Please enter the correct file path")
            return 0
        
class Key_generate:
    
    def write_key():
        """
      Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        key = open("key.key", "rb").read()
        print(key)
