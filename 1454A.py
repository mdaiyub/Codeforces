def my_function(t):
    for i in range(t):
        n = int(input())
        arr = list(range(1, n))
        print(n,end=" ")
        print(*arr)
aiyub = int(input())
my_function(aiyub)
