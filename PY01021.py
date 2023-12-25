t = int(input())

for i in range(t):
    s = input()
    n = len(s)
    a = []
    res = 0
    for i in range(n):
        try:
            x = int(s[i])
            res += x
        except:
            a.append(s[i])
    
    a.sort()
    for i in a:
        print(i, end = "")
    print(res)