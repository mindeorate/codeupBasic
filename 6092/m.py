a = int(input())
randomC = list(map(int, input().split()))
number = [0] * 24

for i in range(a):
    number[randomC[i]] += 1 #출석 횟수 세기

for i in range(1, 24):
    print(number[i], end=' ') #번호가 나온만큼 출력
