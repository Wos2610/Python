s = input()
n = len(s)
a = []
b = [0] * 1000
for i in range(0, n, 2):
    x = s[i:i + 2]
    if len(x) == 2:
        tmp = int(x)
        if tmp not in a:
            a.append(tmp)
            b[tmp] = 1
        else:
            b[tmp] += 1
            
for i in a:
    print('{} {}'.format(i, b[i]))