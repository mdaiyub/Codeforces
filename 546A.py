k,n,w = map(int,input().split())
count = 0
for i in range(w):
    count += ((i+1)*k)
if (count-n)<1:
    print('0')
else:
    print(count - n)


