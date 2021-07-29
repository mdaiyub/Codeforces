l = list(map(int,input().split()))
s = input()
count = 0
for i in s:
    if i=='1':
        count += l[0]
    elif i=='2':
        count += l[1]
    elif i == '3':
        count += l[2]
    elif i=='4':
        count += l[3]

print(count)


