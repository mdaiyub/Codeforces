n = int(input())
b = []

for i in range(n):
    a = int(input())
    b.append(a)

for j in b:
    if j > 2 and j % 2 == 0:
        print((j // 2) - 1)
    elif j > 2 and j % 2 == 1:
        print(j // 2)
    else:
        print(0)



