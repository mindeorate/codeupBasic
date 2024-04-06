a1, a2, a3 = map(int, input().split())
x = int(a1 + a2 + a3) #합
y = (a1 + a2 + a3)/3 #평균
print(x, "%.2f" % y) #평균 <-2번째자리에서 반올림
