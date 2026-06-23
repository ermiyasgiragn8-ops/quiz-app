import base64
import hashlib
import os
from cryptography.fernet import Fernet


def load_key():

    if not os.path.exists("key.key"):
        with open("key.key", "wb") as file_key:
            file_key.write(Fernet.generate_key())

    with open("key.key", "rb") as file_key:
        return file_key.read()


master_pwd = input("what is the master password? ")


key_base = load_key() + master_pwd.encode()
raw_32_bytes = hashlib.sha256(key_base).digest()
fernet_key = base64.urlsafe_b64encode(raw_32_bytes)
fer = Fernet(fernet_key)


def check():
    if not os.path.exists("masters.txt"):
        with open("masters.txt", "w") as f:
            f.write(fer.encrypt(b"authenticated_user").decode())
        print("Master password registered successfully.")
        return True

    try:
        with open("masters.txt", "r") as f:
            token = f.read()
        fer.decrypt(token.encode())
        print("Access Granted!")
        return True
    except Exception:
        print("Access Denied: Invalid Master Password.")
        return False


def add():
    name = input("account name: ")
    pwd = input("password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open("passwords.txt", "a") as file:
        file.write(name + "|" + encrypted_pwd + "\n")
    print(f"Successfully saved password for {name}!")


def view():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet.")
        return

    print("\n--- SAVED PASSWORDS ---")
    with open("passwords.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            if not data or "|" not in data:
                continue
            user, passw = data.split("|")

            try:
                decrypted_pwd = fer.decrypt(passw.encode()).decode()
                print(f"User: {user}, Password: {decrypted_pwd}")
            except Exception:
                print(f"User: {user}, Password: [Error Decrypting Data]")
    print("-----------------------\n")


if check():
    while True:
        mode = (
            input(
                "would you like to add a new password or view existing ones? (view, add), press 'q' to quit: "
            )
            .strip()
            .lower()
        )

        if mode == "q":
            print("thank you for your time :)")
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode.")
else:
    print("Exiting program.")
