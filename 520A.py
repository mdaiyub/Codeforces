n = int(input())
st = str(input().lower())
s = set(st)
ss = sorted(s)
letter = 'abcdefghijklmnopqrstuvwxyz'
z = 0

for i in ss:
    if i==letter[z]:
        z += 1
if z==26:
    print("YES")
else:
    print("NO")
