n = int(input())
a = 'I hate'
b = 'I love'
c = ' that '
d = ' it'
list = str()
for i in range(1,n+1):
    if i%2 != 0:
        list += a
    elif i%2== 0 and i<n:
        list += c+b+c
    else:
        list += c+b

print(list+d)


