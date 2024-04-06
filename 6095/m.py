badukpan = [[0] * 20 for _ in range(20)]
white = int(input())

for _ in range(white):
    x, y = map(int, input().split())
    badukpan[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(badukpan[i][j], end=' ')
    print() 
