import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# ---------- SETUP ----------

SALT_FILE = "./password_manager/salt.bin"
PASSWORD_FILE = "./password_manager/passwords.txt"

def get_salt():
    """Load existing salt or create one if missing."""
    if not os.path.exists(SALT_FILE):
        salt = os.urandom(16)
        with open(SALT_FILE, "wb") as f:
            f.write(salt)
    else:
        with open(SALT_FILE, "rb") as f:
            salt = f.read()
    return salt

def derive_key_from_master(master_password):
    """Turn master password into a Fernet-compatible key."""
    salt = get_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key

# ---------- APP LOGIC ----------

master_password = input("Enter master password: ")
key = derive_key_from_master(master_password)
fernet = Fernet(key)

def add_new_password():
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data = f"Website: {website}|Username: {username}|Password: {password}"
    encrypted = fernet.encrypt(data.encode()).decode()

    with open(PASSWORD_FILE, "a") as f:
        f.write(encrypted + "\n")

    print("Password saved and encrypted successfully.")

def view_existing_password():
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords stored yet.")
        return

    with open(PASSWORD_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("No passwords stored.")
        return

    for line in lines:
        line = line.strip()
        try:
            decrypted = fernet.decrypt(line.encode()).decode()
            print(decrypted)
        except Exception:
            print("⚠️ Could not decrypt (wrong master password or corrupt entry).")

# ---------- MAIN LOOP ----------

while True:
    user_input = input("Would you like to add a new password or view existing ones (add/view) or quit (q): ").lower()

    if user_input == "q":
        break
    elif user_input == "add":
        add_new_password()
    elif user_input == "view":
        view_existing_password()
    else:
        print("Invalid input. Try again.")
