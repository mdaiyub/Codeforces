n = int(input())
a = []
b = []
s = 0
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

for i in a:
    for j in b:
        if i==j:
            s += 1


print(s)