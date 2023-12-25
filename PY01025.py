s = input()

n = len(s)
d = 0
for i in range(n - 1, -1, -1):
    d += 1
    if d == 3 and i > 0:
        s = s[:i] + ',' + s[i:]
        d = 0
print(s)
        

