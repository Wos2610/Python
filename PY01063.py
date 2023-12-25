
def check(s, s0):
    n = len(s)
    m = len(s0)
    i = 0
    res = 0
    while i <= n - m:
        d = 0
        for j in range(m):
            if s[i + j] == s0[j]:
                d += 1
        if d == m:
            res += 1
            i += m
        else:
            i += 1 
    print(res)
            
t = int(input())
while t > 0:
    t -= 1
    s = input()
    s0 = input()
    check(s, s0)