n,h = (map(int,input().split()))
a = list(map(int,input().split()))
count = 0
for i in a:
    if i > h:
        count += 2
    else:
        count += 1
print(count)
