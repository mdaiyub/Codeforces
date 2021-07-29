n = int(input())
for i in range(n+1, 10000):
    s = list(str(i))
    if s[0]!=s[1] and s[0]!=s[2] and s[0]!=s[3] and s[1]!=s[2] and s[1]!=s[3] and s[2]!=s[3]:
        print(int(i))
        exit(0)