n = int(input())
s = str(input())
count1 = 0
count2 = 0

for i in range (len(s)):
    if (s[i]=='A') > (s[i]=='D'):
        count1 += 1


    elif (s[i]=='A') < (s[i]=='D'):
        count2 += 1


if count1 > count2:
    print("Anton")

elif count1 < count2:
    print("Danik")

else:
    print("Friendship")


