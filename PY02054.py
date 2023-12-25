n, m = input().split()
n = int(n)
m = int(m)

a = [[0] * m for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

if n >= m:
    k = n - m
    for i in range(n):
        if k != 0:
            if i % 2 != 0:
                for j in range(m):
                    print(a[i][j], end = " ")
                print()
                k -= 1
        else:        
            for j in range(m):
                print(a[i][j], end = " ")
            print()
else:
    k = m - n
    b = [0] * m
    for j in range(m):
        if j % 2 != 0:
            b[j] = 1
            k -= 1
            if k == 0:
                break
            
    for i in range(n):
        for j in range(m):
            if b[j] == 0:
                print(a[i][j], end = " ")
        print()
    