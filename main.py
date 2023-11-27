import random

x = random.randint(0, 10)

while True:
    y_str = input("Enter an integer: ")
    y = int(y_str)

    if x == y:
        print("Correct!")
        break
    elif x > y:
        print("Too low")
    else:
        print("Too high")
