n = input()
d = 0
if len(n) == 1:
    d = 1
while len(n) > 1:
    res = 0
    for i in range(len(n)):
        res += (ord(n[i]) - ord('0'))
    n = str(res)
    d += 1

print(d)
    