t = int(input())

for i in range(t):
    a,b = map(int,input().split())

    if a==b:
        print(0)

    elif a<b:
        k = b - a
        s = k // 10
        if (s * 10) < k:
            print(s+1)
        else:
            print(s)

    elif a==b:
        print(0)

    elif a>b:
        k = a - b
        s = k // 10
        if (s * 10) < k:
            print(s+1)
        else:
            print(s)



