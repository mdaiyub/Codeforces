l = input()
s = list(l)
st = set()

for i in s:
    if i!="{" and i!="}" and i!="," and i!=" ":
        st.add(i)

print(len(st))
