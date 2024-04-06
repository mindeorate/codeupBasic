n = int(input())
#initialize
a = 0
b = 1
while True :
  a += b
  b += 1
  if a>=n :
    break

print(a)
