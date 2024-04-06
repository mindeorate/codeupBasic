a = map(int, input().split())
#or연산식
b = 0
for a in a:
    b |= a # a의 or연산 -> b

print(b)
