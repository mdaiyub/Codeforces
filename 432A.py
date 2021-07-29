n,k = map(int,input().split())
m = list(map(int,input().split()))
m.sort()

count = 0
for i in m:
    if (i+k) <= 5:
        count += 1

print(count//3)
