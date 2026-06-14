import random
count = 0
number = random.randint(1,50)
while True:
    your_guess = int(input("Guess a number: "))
    if your_guess > number:
        print("Too high")
        count += 1
    elif your_guess < number:
        print("Too low")
        count += 1
    else:
        print("YOU WIN!")
        break
print("No of attempts: ", count)
