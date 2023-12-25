from collections import deque
def check(n):
    s = str(n)
    d = 0
    for i in s:
        if i == '2': d += 1
        if d > len(s)/2: return True    
    return False

a = deque()
b = []
def sinh():
    a.append(1)
    a.append(2)
    
    while True:
        tmp = a.popleft()
        if check(tmp) : b.append(tmp)
        if tmp * 10 > 10**10: break
        a.append(tmp * 10)
        a.append(tmp * 10 + 1)
        a.append(tmp * 10 + 2)

sinh()
t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n):
        print(b[j], end = " ")
    print()
        
        