t = int(input())
while t > 0:
    t -= 1
    n, m = input().split()
    n = int(n)
    m = int(m)

    a = [[0] * m for _ in range(n)]
    b = [[0] * n for _ in range(m)]

    for i in range(n):
        a[i] = [int(x) for x in input().split()]
        
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]
            
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = 0
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]

    for i in range(n):
        for j in range(n):
            print(res[i][j], end = " ")
        print()