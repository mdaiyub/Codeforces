a,b,c,d = map(int,input().split())
s = max(a,b,c,d)

if s==a:
    x1 = s-b
    x2 = c-x1
    x3 = d-x1

elif s==b:
    x1 = s-a
    x2 = c-x1
    x3 = d-x1

elif s==c:
    x1 = s-a
    x2 = b-x1
    x3 = d-x1

elif s==d:
    x1 = s-a
    x2 = b-x1
    x3 = c-x1


print(x1, x2, x3)