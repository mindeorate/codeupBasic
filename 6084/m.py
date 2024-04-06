a, b, c, d = map(int, input().split())
s = (a * b * c * d) / (8 * 1024 * 1024) #계산식
print('%.1f MB' % s) #소수 첫번째자리까지
