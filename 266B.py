a,b=map(int,input().split())
s =list(input())
for i in range(b):
    x=0
    while x<a-1:
        if s[x]=='B' and s[x+1]=='G':
            s[x]='G'
            s[x+1]='B'
            x+=2
        else:
            x+=1
print(''.join(s))