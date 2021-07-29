n = int(input())
a = list(map(int,input().split()))
sereja,dima = 0,0
for i in range(n):
    if a[0] >= a[len(a)-1]:
        if i%2==0:
            sereja += a[0]
        else:
            dima += a[0]
        del a[0]

    else:
        if i%2 == 0:
            sereja += a[len(a)-1]
        else:
            dima += a[len(a)-1]
        del a[len(a)-1]
print(sereja,dima)