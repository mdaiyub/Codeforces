a,b = map(int,input().split())
s = 1
for i in range(1,1001):
    n = a*i
    if n%10==0 or (n%10==b):
        print(s)
        break

    else:
        s+=1

