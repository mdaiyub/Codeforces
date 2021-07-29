for i in range(int(input())):
    k = input()
    if len(k)==1:
        print((int(k[0])-1)*10+1)
    elif len(k)==2:
        print((int(k[0])-1)*10+3)
    elif len(k)==3:
        print((int(k[0])-1)*10+6)
    elif len(k)==4:
        print((int(k[0])-1)*10+10)
