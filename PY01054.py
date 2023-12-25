t = int(input())
while t > 0:
    t -= 1
    s = input()
    k = len(s)
    res = 1
    for i in range(k):
        if s[i] != '0': res = res * int(s[i])
    print(res)
    