import random
import string

passLen = 4
passVal = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(passLen):
    password += random.choice(passVal)

print("Random Password = ",password)