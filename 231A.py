n = int(input())
count = 0
for i in range (n):
    x = input()
    sum = int(x[0]) + int(x[2]) + int(x[4])
    if sum >= 2:
        count += 1
print(count)