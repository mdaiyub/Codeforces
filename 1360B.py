for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    s.sort()
    minx = 999999
    for j in range(len(s)-1):
        x = s[j+1] - s[j]
        if x < minx:
            minx = x
    print(minx)
