#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = abs(number) % 10
print(f"Last digit of {number} is {rem}", end=' ')
if rem > 5:
    print("and is greater than 5")
elif rem == 0:
    print("and is 0")
elif rem < 6 and rem != 0:
    print("and is less than 6 and not 0")
