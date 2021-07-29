ans=0
matrix= [[0,0,0,0,0], [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
for i in range(5):
    s= input().split()
    for j in range(5):
        matrix[i][j]=int(s[j])
        if matrix[i][j]==1:
            ans= (abs(i-2)+ abs(j-2))
print (ans)