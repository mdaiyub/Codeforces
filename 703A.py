n = int(input())

miskha = 0
chris = 0

for i in range(n):
    m,c = list(map(int,input().split()))
    if m > c:
        miskha += 1
    elif m < c:
        chris += 1
if miskha > chris:
    print('Mishka')
elif miskha < chris:
    print('Chris')
else:
    print('Friendship is magic!^^')
