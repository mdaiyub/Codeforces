t = int(input())

for i in range(t):
    x,y,n = map(int,input().split())
    a = int((n-y)/x)
    b = (a*x)+y
    print(b)