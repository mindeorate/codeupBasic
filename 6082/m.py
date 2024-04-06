a = int(input())

for i in range(1, a + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print("X", end=' ')  # 3, 6, 9가 포함된 경우 X
    else:
        print(i, end=' ')  # 그 외의 경우
