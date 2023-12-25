f = open('DATA.in', 'r')

lines = f.read().split()
res = []
for i in lines:
    a = i.split(" ")
    for j in a:
        try:
            x = int(j)
            if x > (2**63 - 1): res.append(j)
        except:
            res.append(j)

res.sort()
for i in res:
    print(i, end = " ")
