import random
print("Random vs You. Input a number [1;10]")
while True:
    a = random.randint(1, 10)
    try:
        b = int(input(""))
    except ValueError:
        print("Data must be integer")
    else:
        if a == b:
            print(f"Your number {b} \n Number of comp: {a} \n You are win!")
            break
        else:
            print(f"Your number {b} \n Number of comp: {a} \n Try again!")