count = 0
for i in range (int(input())):
    bit = input()
    if '++' in bit:
        count += 1
    elif '--' in bit:
        count -= 1
print(count)

