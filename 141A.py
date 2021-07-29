a = (input())
b = (input())

main = list(input())
main.sort()

guest = list(a+b)
guest.sort()

if guest==main:
    print("YES")
else:
    print("NO")