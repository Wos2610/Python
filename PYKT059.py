a = []
n, m, x = list(map(int, input().split()))
for i in range(0, n + 1):
    a.append([])
for i in range(m):
    c, d = list(map(int, input().split()))
    a[c].append(d)
    a[d].append(c)

mark = [0] * (n + 6)   
def dfs(i):
    mark[i] = 1
    for j in a[i]:
        if mark[j] == 0:
            dfs(j)

dfs(x)
for i in range(1, n + 1):
    if mark[i] == 0:
        print(i)
