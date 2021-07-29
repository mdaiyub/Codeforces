n = int(input())
count = 1
st = []

for i in range(n):
    a = int(input())
    st.append(a)

for i in range(1,n):
    if not st[i] == st[i-1]:
        count += 1

print(count)