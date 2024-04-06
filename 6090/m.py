a, m, d, n = map(int, input().split())
c = a
for _ in range(1, n): # _ : 반복횟수 무시
    c = c * m + d
print(c)
