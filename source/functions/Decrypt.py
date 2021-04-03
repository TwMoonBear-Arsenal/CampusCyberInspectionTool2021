from cryptography.fernet import Fernet
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