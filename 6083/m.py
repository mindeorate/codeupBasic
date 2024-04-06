from itertools import product #이터레이터 함수 라이브러리

a, b, c = map(int, input().split())

#initialize
count = 0

for color in product(range(a), range(b), range(c)):
    print(*color)  # RGB 색의 모든 정보 출력
    count += 1  

print(count)
