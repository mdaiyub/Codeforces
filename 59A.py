s = input()
upper = 0
lower = 0
for aiyub in (s):#lower case  can count by (islower())
    if(aiyub.isupper()):#Upper case counting by (isupper())
        upper += 1
    else:
        lower += 1
if(upper>lower):
    print(s.upper())
else:
    print(s.lower())