n = int(input())
a = []

while True:
    try:
        a += list(map(int, input().split()))
    except:
        break

mark = [0] * (n + 6)
b = []
c = []
for i in range(n):
    if a[i] % 2 == 0:
        b.append(a[i])
        mark[i] = 1
    else:
        c.append(a[i])
        
b.sort()
c.sort(reverse=True)

for i in range(n):
    if mark[i] == 1:
        print(b.pop(0), end = " ")
    else:
        print(c.pop(0), end = " ")