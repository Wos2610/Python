def doi(s):
    res = 0
    dv = 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            res += dv
        dv *= 2
    return res

s = input()
while len(s) % 3 != 0: s = "0" + s
n = len(s)

for i in range(0, n, 3):
    print(doi(s[i:(i + 3)]), end = "")

