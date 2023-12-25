n, m = input().split()
n = int(n)
m = int(m)
a = [[0] * m for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))
    
mi = 10001
ma = -1

for i in range(n):
    for j in range(m):
        mi = min(mi, a[i][j])
        ma = max(ma, a[i][j])

k = ma - mi
d = 0   
for i in range(n):
    for j in range(m):
        if a[i][j] == k:
            if d == 0: print(k)
            d += 1
            print(f"Vi tri [{i}][{j}]")

if d == 0:
    print("NOT FOUND")
    