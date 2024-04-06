a = input()
b = int(a, 16) # a --> 16진수

for i in range(1, 16):
    c = b * i
    print('%X'%b, '*%X'%i, '=%X'%(c), sep='') # <-- 제시된 조건(?)임
