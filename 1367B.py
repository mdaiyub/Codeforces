t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    even = 0
    odd = 0
    for j in range(n):
        if j % 2 == 0:
            if a[j]%2 != 0:
                even += 1

        else:
            if a[j]%2 == 0:
                odd += 1


    if even == odd:
        print(even)
    else:
        print(-1)
