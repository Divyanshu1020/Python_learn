import os

SALT_SIZE = 16

salt = os.urandom(SALT_SIZE)
print(salt)