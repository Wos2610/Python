import math
t = int(input())

while t > 0:
    t -= 1
    a = []
    n = int(input())
    while len(a) < n:
        a.append(int(input()))
        
    m = [0] * 1006
    
    for i in a:
        m[i] += 1
    maxx= 0
    ind = 0
    for i in m:
        if(maxx < i):
            maxx = i
            ind = m.index(i)
    print(ind)
