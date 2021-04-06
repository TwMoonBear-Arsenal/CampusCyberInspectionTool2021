from cryptography.fernet import Fernet
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
