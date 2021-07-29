n = input()
x = 0
for i in range (len(n)):
    if int(n[i])==4 or int(n[i])==7:
        x+=1
if x==4 or x==7:
    print("YES")
else:
    print("NO")

print((x))