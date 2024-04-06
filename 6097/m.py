a, b = map(int, input().split())
grid = [[0] * b for _ in range(a)]
n = int(input())

for _ in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0:
        for i in range(l):
            grid[x - 1][y - 1 + i] = 1
    else:
        for i in range(l):
            grid[x - 1 + i][y - 1] = 1

for row in grid:
    print(*row)
