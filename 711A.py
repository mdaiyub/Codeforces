x = int(input())

a = []
for i in range(x):
    a.append(str(input()))
n = 0
for v in range(x):
    place = a[v]
    place = place.split("|")
    if place[0] == "OO":
        n = 1
        a[v] = "++|" + place[1]
        break
    elif place[1] == "OO":
        n = 1
        a[v] = place[0] + "|++"
        break
    else:
        pass
if n == 0:
    print("NO")
else:
    print("YES")
    for i in range(x):
        print(a[i])


