def isThuanNghich(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n - i - 1]: return False
    return True

f = open('VANBAN.in', 'r')
m = f.read().split()
a = {}
for i in m:
    if isThuanNghich(i):
        if a.get(i) is None: a[i] = 1
        else: a[i] += 1

maxx = 0
for i in a:
    maxx = max(maxx, len(i))
    
mark = {}
for i in m:
    if a.get(i) is not None and len(i) == maxx:
        if mark.get(i) is None: 
            print(i + " " + str(a[i]))
            mark[i] = 1

