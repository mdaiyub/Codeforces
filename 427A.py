n = int(input())

ar = list(map(int, input().split()))

hired = 0
untreated = 0
for i in ar:
    if i > 0:
        hired += i
    else:
        if hired == 0:
            untreated += 1
        else:
            hired -= 1
print(untreated)