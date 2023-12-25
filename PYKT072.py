n = int(input())

a = []
for i in range(n):
    a.append(input())

def tinh(a, b):
    if a == b: return 0
    for i in range(len(a)):
        b = b[1:] + b[0]
        if a == b: return i + 1
        
    return -1
mark = 0
res = 9999999999999

for i in range(n):
    d = 0
    for j in range(n):
        if i == j: continue
        tmp = tinh(a[i], a[j])
        if tmp == -1:
            mark = 1
            break
        d += tmp
    res = min(res, d)

if mark == 0:
    print(res)
else:
    print("-1")
        
        