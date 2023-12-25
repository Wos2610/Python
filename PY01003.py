def check(s):
    n = len(s)
    if n == 1: return s
    l = list(s)
    for i in range(n - 1, 0, -1):
        if l[i] >= '5':
            l[i - 1] = chr(ord(l[i - 1]) + 1)
            
    if l[1] >= '5':
        l[0] = chr(ord(l[0]) + 1)
    
    for i in range(2, n):
        l[i] = '0'
            
    return ''.join(l)

t = int(input())
while t > 0:
    t -= 1
    s = input()
    print(check(s))