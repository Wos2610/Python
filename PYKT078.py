t = int(input())

for i in range(t):
    n, m = input().split()
    n = int(n)
    m = int(m)
    a = list(map(int, input().split()))
    maxx = max(a)
    for i in range(n):
        if a[i] == maxx:
            a.insert(i, m)
            break
    b = []
    c = []
    for i in a:
        if i < 0:
            b.append(i)
        else:
            c.append(i)
    
    for i in b:
        print(i, end=" ")
    for i in c:
        print(i, end=" ")
    print()