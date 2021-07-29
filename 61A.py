n = input('')
k = input('')
ln = len(n)
z = ''
for i in range(ln):
    if n[i]==k[i]:
        z+='0'
    else:
        z+='1'

print(z)