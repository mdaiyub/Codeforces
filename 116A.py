n = 0
m = 0
for i in range(int(input())):
    a,b = map(int, input().split())
    n = n-a
    n = n+b
    if (n>=m):
        m = n
print(m)




