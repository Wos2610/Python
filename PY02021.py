class Num:
    def __init__(self, s, x, y, z):
        self.s = s
        self.x = x
        self.y = y
        self.z = z
    def __lt__(self, other):
        return self.s < other.s
    def __str__(self):
        return str(self.s)
    
t = int(input())
for i in range(t):
    a = []
    n, m, k = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    
    p1, p2, p3, ok = 0, 0, 0, 0
    while p1 < n and p2 < m and p3 < k:
        if b[p1] == c[p2] and c[p2] == d[p3]:
            print(b[p1], end = " ")
            ok = 1
            p1 += 1
            p2 += 1
            p3 += 1
        elif b[p1] < c[p2]:
            p1 += 1
        elif c[p2] < d[p3]:
            p2 += 1
        elif d[p3] < b[p1]:
            p3 += 1
    if ok == 0: print("NO")
    else: print()
    

    
       
            