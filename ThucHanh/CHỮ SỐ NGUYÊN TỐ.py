      
b = [2, 3, 5, 7]
def hoanVi(i, m, a):
    if i > m:
        x = set(a[1:])
        if len(x) != 4: return
        for j in range(1, m + 1):
            print(a[j], end = "")
        print()
        return
    
    for j in range(0, 4):
        if j == 0 and i == m: continue
        a[i] = b[j]
        hoanVi(i + 1, m, a)

n = int(input())
for i in range(4, n + 1):
    a = [0] * (i + 1)
    hoanVi(1, i, a)