n = int(input())
z = int(n/2)
lst = list()
for i in range(1,z+1):
    e = n-i
    if e%i==0:
        lst.append(i)

print(len(lst))
