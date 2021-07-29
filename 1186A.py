def state(participant,pen,notebook):
    if participant <= pen and participant <= notebook:
        print('Yes')
    else:
        print('No')


a,b,c = list(map(int,input().split()))
state(a,b,c)
