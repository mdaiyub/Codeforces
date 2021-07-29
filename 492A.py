n = int(input())
s = 0
d = 0
r = 0
for i in range(1,n+1):
    s = s+i
    d += s
    if d > n:
       break
    elif d==n:
        r += 1
        break
    r += 1



print(r)


