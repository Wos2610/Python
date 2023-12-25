f = open('STRING.in', 'r')

t = int(f.readline())

for i in range(t):
    s1 = f.readline().strip()
    s2 = f.readline().strip()
    
    n = len(s1)
    m = len(s2)
    if n >= m:
        for i in range(n - m + 1):
            tmp = s1[i : i + m]
            if tmp == s2: print(i + 1, end = " ")
        print()