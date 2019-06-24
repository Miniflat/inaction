def check_input(x, y):
    if 0 <= x <= 2 and 0 <= y <= 2:
        return True
    else:
        return False


def make_turn(a, x, y, player):
    for i in range(len(a)):
        for j in range(len(a)):
            if i == x and j == y and player == 0:
                a[i][j] = 0
                return True
            elif i == x and j == y and player == 1:
                a[i][j] = 1
                return True
            elif a[x][y] == 0 or a[x][y] == 1:
                return False
            else:
                continue


def check_draw(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] != -1:
                print("Game is over. Draw!")
                return True
    exit()


def check_win(a, player):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][0] == a[i][1] == a[i][2] == player:
                return True
            if a[0][j] == a[1][j] == a[2][j] == player:
                return True
            if a[0][0] == a[1][1] == a[2][2] == player:
                return True
            if a[0][2] == a[1][1] == a[2][0] == player:
                return True
            else:
                return False


def print_grid(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == -1:
                print('_', end='|')
            elif a[i][j] == 0:
                print('X', end='|')
            elif a[i][j] == 1:
                print('0', end='|')
            else:
                print(a[i][j], end='_')
        print()