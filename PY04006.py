import math
class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
class Triangle:
    def __init__(self, ab, ac, bc):
        self.ab = ab   
        self.ac = ac
        self.bc = bc
    
    def chuvi(self):
        if self.ab + self.ac > self.bc and self.ab + self.bc > self.ac and self.ac + self.bc > self.ab:
            print("{:.2f}".format(1/4 * math.sqrt((self.ab + self.ac + self.bc) * (self.ab + self.bc - self.ac) * (self.ab - self.bc + self.ac) * (- self.ab + self.bc + self.ac ))))
        else: print("INVALID")
        
n = int(input())

while n > 0:
    n -= 1
    a = [float(x) for x in input().split()]
    ab = Point(a[0], a[1], a[2], a[3]).x
    ac = Point(a[0], a[1], a[4], a[5]).x
    bc = Point(a[2], a[3], a[4], a[5]).x
    
    Triangle(ab, ac, bc).chuvi()
        