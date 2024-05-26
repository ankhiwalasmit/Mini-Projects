import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

# 1st method
password = ""
for i in range(pass_len):
    password += random.choice(charValues)

# 2nd method: list comprehension
password = "".join([random.choice(charValues) for i in range(pass_len)])

print("your random password is:", password)