for i in range(int(input())):
    x,y,z = sorted(list(map(int,input().split())))
    if y==z:
        print("YES")
        print(x,y,1)
    else:
        print("NO")
