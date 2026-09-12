import random

num1=random.randint(1,10)

while True:
    num2=int(input("Guess the number(1-10):"))

    if num2 == num1:
        print("Correct!")
        break

    elif num2 < num1:
        print("Too low!")

    else:
        print("Too High!")
        



