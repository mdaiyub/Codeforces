a,b,c = map(int,input().split())
for_sr = a,b,c
sr = list(sorted(for_sr))

first = sr[1] - sr[0]
second = sr[2] - sr[1]

print(first+second)