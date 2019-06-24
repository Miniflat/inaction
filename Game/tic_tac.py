from Game.modules import *

a = [[-1 for i in range(3)] for j in range(3)]
print(a)
count = 0
while count < 9:
    while True:
        try:
            x = int(input())
            y = int(input())
        except (ValueError, TypeError):
            print("ValueError or TypeError")
        else:
            if not check_input(x,y):
                print("Error input, try again")
                continue
            if not make_turn(a, x, y, 0):
                print("Cell busy, try again")
                continue
            break
    count += 1
    if check_win(a, 0):
        print("Game is over. Player number 1 WIN!")
        print_grid(a)
        exit()
    print_grid(a)

    while True:
        try:
            x = int(input())
            y = int(input())
        except (ValueError, TypeError):
            print("ValueError or TypeError")
        else:
            if not check_input(x, y):
                print("Error input, try again")
                continue
            if not make_turn(a, x, y, 1):
                print("Cell busy, try again")
                continue
            break
    count += 1
    if check_win(a, 1):
        print("Game is over. Player number 2 WIN!")
        print_grid(a)
        exit()
    print_grid(a)
    if count == 8:
        check_draw(a)
        break