from cryptography.fernet import Fernet
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
        
