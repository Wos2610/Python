import math
class Vector:
    def __init__(self, x):
        self.x = x
    
    def kc(self, a):
        n = len(self.x)
        res = 0
        for i in range(n):
            res += (self.x[i] - a.x[i]) ** 2
        res = math.sqrt(res)
        return res
    
    def voHuong(self, a):
        n = len(self.x)
        res = 0
        for i in range(n):
            res += (self.x[i] * a.x[i])
        return res
    
t = int(input())
for i in range(t):
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b0 = Vector(b)
    c0 = Vector(c)
    print('{:.2f} {}'.format(b0.kc(c0), b0.voHuong(c0)))
    
