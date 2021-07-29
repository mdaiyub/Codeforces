n = int(input())
count = 0
for i in range(n):
    a = input()
    if a=='Tetrahedron':
        count += 4
    elif a=='Cube':
        count += 6
    elif a=='Octahedron':
        count += 8
    elif a=='Dodecahedron':
        count += 12
    elif a=='Icosahedron':
        count += 20

print(count)