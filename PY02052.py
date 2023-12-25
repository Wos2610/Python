n = int(input())
a = [[0] * n for _ in range (n)]

for i in range(n):
    a[i] = list(map(int, input().split()))
    
k = int(input())

tren = 0
duoi = 0
for i in range(n):
    for j in range(i + 1, n):
        tren += a[i][j]
        
for i in range(n):
    for j in range(i):
        duoi += a[i][j]
        
res = abs(tren - duoi)
if res <= k:
    print("YES")
else:
    print("NO")
print(res)
        