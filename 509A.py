n = int(input())
if n == 1:
    print(1)
else:

    a = b = 1
    for i in range(1, n):
        a *= i
    for i in range(1, 2 * n - 1):
        b *= i
    print(int(b / a ** 2))

