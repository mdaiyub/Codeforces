n, k, l, c, d, p, nl, np = map(int,input().split())
Frnds_have = k*l

Each_needs = Frnds_have//nl

limes = c*d

toasts = p//np

ans = min(Each_needs,limes,toasts)//n
print(ans)