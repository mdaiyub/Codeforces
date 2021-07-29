n = int(input())
for i in range(n):
    input()
    s = list(input().split(' '))
    prov = []
    d = []
    for k in s:
        if k not in prov:
            d.append(k)
            prov.append(k)
        else:
            prov.remove(k)
    print(' '.join(d))