n,k = map(int,input().split())
w = 0

for i in range(1,n+1):
    k += 5*i
    if k > 240:
        break
    else:
        w += 1

print(w)







