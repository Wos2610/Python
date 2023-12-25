n = int(input())
a = []
while len(a) != n:
    a.extend(list(map(int, input().split())))
    
b = [0] * n
c = []
d = []
for i in range(n):
    if a[i] % 2 == 0:
        b[i] = 1
        c.append(a[i])
    else:
        d.append(a[i])
c.sort()
d.sort(reverse=True)

for i in range(n):
    if b[i] == 1:
        print(c.pop(0), end = " ")
    else:
        print(d.pop(0), end = " ")

