import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        
n, m = input().split()
n = int(n)
m = int(m)

a = [[0] * m for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))
    
mark = 0
res = 0
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]):
            mark = 1
            res = max(res, a[i][j])

if mark == 1: print(res)
for i in range(n):
    for j in range(m):
        if a[i][j] == res:
            print(f"Vi tri [{i}][{j}]")
            
if mark == 0: print("NOT FOUND")
    
