for i in range(int(input())):
    a,b,c,n = map(int,input().split())
    d = a+b+c+n
    if (d%3==0) and (max(a,b,c)<= d//3):
        print("YES")
    else:
        print("NO")