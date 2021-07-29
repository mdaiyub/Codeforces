t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    even = 0
    odd = 0
    for j in a:
        if j%2==0:
            even += 1
        else:
            odd += 1

    if sum(a)%2 != 0:
        print("YES")
    else:
        if odd > 0 and even > 0:
            print("YES")
        else:
            print("NO")





