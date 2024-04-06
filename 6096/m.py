baduk = [list(map(int, input().split())) for _ in range(19)]
count = int(input())

for _ in range(count):
    x, y = map(int, input().split())
    for j in range(19):
        baduk[x-1][j] = 1 - baduk[x-1][j]  # 가로
        baduk[j][y-1] = 1 - baduk[j][y-1]  # 세로
for row in baduk:
    print(*row) #*row : row열 구분 ex) [1,0,1] --> 1 0 1
