n = int(input())
a = input().split()
b = []

for i in range(n):
    a[i] = int(a[i])
    b.append(0)

for i in range(n):
    b[a[i]-1] = i+1

for i in range (n):
    print(b[i],end =' ')


