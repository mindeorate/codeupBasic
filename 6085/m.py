a, b, c = map(int, input().split())
s = (a * b * c) / (8 * 1024 * 1024)
print('%.2f MB' % s) #소수점 3번째에서 반올림
