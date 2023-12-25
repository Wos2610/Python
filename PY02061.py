t = int(input())

while t > 0:
    t -= 1
    
    n, m = input().split()
    n = int(n)
    m = int(m)

    a = []
    b = []

    for i in range(0, n):
        tmp = [int(x) for x in input().split()]
        a.append(tmp)

    for i in range(0, 3):
        tmp = [int(x) for x in input().split()]
        b.append(tmp)
        
    res = 0
    for i in range(0, n - 2):
        for j in range(0, m - 2):
            tmp = 0
            for p in range(0, 3):
                for q in range(0, 3):
                    tmp += (b[p][q] * a[i + p][j + q])
            res += tmp
            
    print(res)
            