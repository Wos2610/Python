def check(n):
    s = str(n)
    if len(s) < 2: return False
    if s == s[::-1]: return True
    return False

n, m = list(map(int, input().split()))
a = []

for i in range(n):
    a.append(list(map(int, input().split())))
    
maxx = -1
for i in range(n):
    for j in range(m):
        if check(a[i][j]):
            maxx = max(maxx, a[i][j])
            
if maxx == -1: print("NOT FOUND")
else:
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print('Vi tri [{}][{}]'.format(i, j))

