n = int(input())

a = []

for i in range(n):
    b = input()
    a.append(b)

res = 0
for i in range(n):
    dem = 0
    for j in range(n):
        if a[i][j] == 'C':
            dem += 1
    res += (dem * (dem - 1)) // 2
    
for j in range(n):
    dem = 0
    for i in range(n):
        if a[i][j] == 'C':
            dem += 1
    res += (dem * (dem - 1)) // 2
    
print(res)