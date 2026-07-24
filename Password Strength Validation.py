"""
Password Strength Validator-> checks a proposed password against standard corporate security rules and scores its strength.
"""

#Creating the checking function for the password
def check_password_strength(*password):
    score = 0

#Length Check
    if len(password) >= 8:
        score += 1

#Number Check (Digits)
    for ele1 in password:
        if ele1.isdigit():
            score += 1
            break

#Case Check (Uppercase & Lowercase)
    for ele2 in password:
        if ele2.isupper():
            score += 1
            break
    for ele3 in password:
        if ele3.islower():
            score += 1
            break

#Special Character Check
    for ele4 in password:
        if ele4 in ['!','@','#','$','%']:
            score += 1
            break

    return score

my_password = input("Enter a password: ").strip()
output = check_password_strength(my_password)

#Checking the score points
if output == 1:
    print("Weak")
elif output in [2,3]:
    print("Moderate")
elif output >= 4:
    print("Strong")
