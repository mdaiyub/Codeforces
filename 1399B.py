t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    mina = min(a)
    minb = min(b)
    count = 0
    for j in range(n):
        x = a[j] - mina
        y = b[j] - minb
        if x < y:
            count += y
        else:
            count += x
    print(count)