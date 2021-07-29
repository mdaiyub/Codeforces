n = int(input())
b = list(map(int,input().split()))
ans = 0
for i in range(n):
    if b[i] == 1:
        ans += 1

if ans > 0:
    print("Hard")
else:
    print('Easy')



