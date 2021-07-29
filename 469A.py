n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = a[1:]
b = b[1:]
for i in range(1,n+1):
    if(i in a or i in b):
        flag = 1
    else:
        flag = 0
        break
if(flag):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')