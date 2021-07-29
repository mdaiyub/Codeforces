n = int(input())
l = list(map(int,input().split()))

max = 0
for i in l:
    if i > max:
        max = i

sum = 0
for i in l:
    sum = sum + (max - i)
print(sum)

