def my_function(n):
    a,b = input(),input()
    ans = 0
    for i in range(n):
        d = abs(int(a[i]) - int(b[i]))
        ans += min(d, 10 - d)
    print(ans)

aiyub = int(input())
my_function(aiyub)
