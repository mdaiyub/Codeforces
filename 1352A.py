for _ in range(int(input())):
    n=int(input())
    k=1
    l = []
    while n!=0:
        if n%10!=0:
            l.append(int(n%10)*k)
        n//=10
        k*=10
    print(len(l))
    print(*l)


