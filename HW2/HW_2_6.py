def make_turn(player, a, x, y):
    for i in range(len(a)):
        for j in range(len(a)):
            if i == x1 and j == y1 and a[i][j] != 0 and player == 0:
                a[i][j] = 1
            elif i == x2 and j == y2 and a[i][j] != 1 and player == 1:
                a[i][j] = 0
            else:
                continue
    return a


count = 0
n = [[-1 for i in range(3)] for j in range(3)]
while count < 9:
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    make_turn(0, n, x1, y1)
    make_turn(1, n, x2, y2)
    print(n)
    count += 1
    if count == 8:
        exit()