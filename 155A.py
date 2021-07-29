n = int(input())
lst = list(map(int,input().split()))
mi = lst[0]
ma = lst[0]
count = 0

for i in range(len(lst)):
    if lst[i]<mi:
        mi = lst[i]
        count += 1

    elif lst[i]>ma:
        ma = lst[i]
        count += 1

print(count)
