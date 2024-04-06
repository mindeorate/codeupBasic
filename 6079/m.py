a = int(input())
amount = 0
count = 1

while True : 
    amount += count
    if amount >= a:
     break
    count += 1

print(count)
