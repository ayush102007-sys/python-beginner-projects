import random
password = []

all_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"

l = int(input("The length of password: "))

for x in range(l):
    password.append(random.choice(all_characters))

password_1 = "".join(password)
print(password_1)






