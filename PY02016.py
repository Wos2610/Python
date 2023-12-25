t = int(input())
for i in range(t):
    n = int(input())
    b = {}
    a = list(map(int, input().split()))
    for i in a:
        if i not in b:
            b[i] = 1
        else:
            b[i] += 1
    maxx = -1
    ind = -1
    for i in b:
        if b[i] > maxx:
            maxx = b[i]
            ind = i
    
    if maxx > n / 2: print(ind)
    else: print("NO")
    
    