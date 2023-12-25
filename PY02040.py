n = int(input())

matrix = []

for i in range(n):
    a = [int(x) for x in input().split()]
    matrix.append(a)
    
k = int(input())

sum1 = 0
for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        sum1 += matrix[i][j]

sum2 = 0
for i in range(1, n):
    for j in range(n - i, n):
        sum2 += matrix[i][j]
      
res = abs(sum1 - sum2)

if res <= k: print("YES")
else: print("NO")
print(res)


