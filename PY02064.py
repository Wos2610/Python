t = int(input())

while t > 0:
    t -= 1
    n, k = input().split()
    n = int(n)
    k = int(k)
    a = list(map(int, input().split()))
    a.sort()
    b = [[0] * 5 for _ in range(k)]

    for i in range(k):
        b[i][4] = a.pop()
    for i in range(k):
        b[i][2] = a.pop()
    for i in range(k):
        b[i][0] = a.pop()
    for i in range(k):
        b[i][1] = a.pop()
    for i in range(k):
        b[i][3] = a.pop()
        
    res = 0
    for i in range(k):
        for j in range (5):
            print(b[i][j], end = " ")
            if j == 1 or j == 3: d = -1
            else: d = 1
            res += b[i][j] * d * (i + 1)
        print()
    print(res)