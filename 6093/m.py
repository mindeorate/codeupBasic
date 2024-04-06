a = int(input())
random = list(map(int, input().split()))

for i in range(a-1, -1, -1): #거꾸로 출력
    print(random[i], end=' ')
