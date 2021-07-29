for i in range(int(input())):
    s = input()
    t = ""
    for i in range(len(s)):
        if i != 0 and i != len(s) - 1 and i % 2 == 0:
            pass
        else:
            t += s[i]

    print(t)
