
import time

t = int(input("Total number of seconds: "))

while t >0 :

    minutes , seconds = divmod(t , 60)

    print(f"The time is {minutes:02d}:{seconds:02d}", end="\r" , flush= True )

    time.sleep(1)
    t -= 1

print("\n Time's up!")







