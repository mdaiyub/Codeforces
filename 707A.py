n,m=map(int,input().split())
color_count=0
for i in range(n):
    x=list(input().split())
    for i in x:
        if i=='C' or i=='M' or i=='Y':
            color_count=1

if color_count>=1:
    print("#Color")
else:
    print("#Black&White")






