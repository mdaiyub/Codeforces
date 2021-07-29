t = int(input())

for i in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = list(map(int,input().split()))
    b.sort()
    b.reverse()
    for i in range(k):
        for i in range(len(b)):
            if a[i] < b[i]:
                a[i] , b[i] = b[i] , a[i]
                break
    print(sum(a))
