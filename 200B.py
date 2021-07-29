n = int(input())
b = list(map(int, input().split()))

x = 0

for i in range(n):
    x += b[i]

print(x/n)