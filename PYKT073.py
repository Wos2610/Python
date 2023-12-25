n = int(input())

a = []
for i in range(n):
    a.append(input())

res = []
d = 0
for i in range(n):
    tmp = a[i].split(" ")
    if i != n - 1:
        tmp1 = a[i + 1].split(" ")
        if len(tmp) == 8 and len(tmp1) != 6:
            res.append(1)
        if len(tmp) == 7:
            d += 1
        if d == 4:
            res.append(2)
            d = 0
    else:
        if len(tmp) == 8:
            res.append(1)
        if len(tmp) == 7:
            res.append(2)

print(len(res))
for i in res:
    print(i)
    