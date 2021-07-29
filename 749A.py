n=int(input())
b=[]
print(int(n/2))
if int(n)%2==0:
    for k in range(int(n/2)):
        b.append('2')
else:
    for k in range(int(n/2)-1):
        b.append('2')
    b.append('3')
print(' '.join(b))
