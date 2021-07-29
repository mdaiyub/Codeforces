n = int(input())
std = list(map(int,input().split()))

t1 = []
t2 = []
t3 = []
for i in range(len(std)):
    if std[i] == 1:
        t1.append(i+1)
    elif std[i] == 2:
        t2.append(i+1)
    elif std[i] == 3:
        t3.append(i+1)

team = min(len(t1),len(t2),len(t3))
print(team)
if team != 0:
    for i in range(team):
        print(t1[i], t2[i], t3[i])

