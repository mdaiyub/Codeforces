t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    mina = min(a,b)
    mina = mina*2
    ma = max(a,b,mina)
    print(ma*ma)






