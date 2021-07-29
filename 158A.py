n,k = map(int,input().split())
count = 0
m = list(map(int,input().split()))
for i in m:
    if i>0 and i>=m[k-1]:
        count += 1
print(count)