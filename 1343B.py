t = int(input())
for i in range(t):
  case = int(input())
  half = case//2
  if half % 2 == 1:
    print("NO")
  else:
    print("YES")
    evens = 2
    odds = 1
    ans = []
    for x in range(half):
      ans.append(evens)
      evens += 2
    for x in range(half - 1):
      ans.append(odds)
      odds += 2
    ans.append(odds + half)
    print(*ans)
