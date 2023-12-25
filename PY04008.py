t = int(input())

a = []
while True:
    try:
        a.extend(map(int, input().strip().split()))
    except:
        break

def tich(a, b, n, m):
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = 0
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]
    return c

for i in range(t):
    n = a[0]
    m = a[1]
    b = [[0] * m for _ in range(n)]
    ind = 2
    for j in range(n):
        for k in range(m):
            b[j][k] = a[ind]
            ind += 1
            
    c = [[0] * n for _ in range(m)]
    for j in range(m):
        for k in range(n):
            c[j][k] = b[k][j]
    
    res = tich(b, c, n, m)
    
    for j in range(n):
        for k in range(n):
            print(res[j][k], end = " ")
        print()

    for j in range(0, n * m + 2):
        a.pop(0)
    