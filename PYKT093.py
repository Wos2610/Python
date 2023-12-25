from math import ceil
class ThiSinh:
    sum = 0
    ma = ""
    xep = 0
    def __init__(self, id, ten, x1, x2, x3):
        self.ma = "SV{:02d}".format(id)
        self.ten = ten
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.tinh()
    
    def chuanHoaTen(self):
        res = ""
        a = self.ten.strip().split()
        for i in range(len(a)):
            res += a[i][:1].upper() + a[i][1:].lower()
            if i != len(a) - 1: res += " "
        return res
    
    def tinh(self):
        self.ten = self.chuanHoaTen()
        self.sum = (3 * self.x1 + 3 * self.x2 + 2 * self.x3) / 8
        self.sum = ceil(self.sum * 100) / 100
        
    def __str__(self):
        return "{} {} {:.2f} {}".format(self.ma, self.ten, self.sum, self.xep)
    
    def __lt__(self, other):
        if self.sum == other.sum: return self.ma < other.ma
        return other.sum < self.sum
    
n = int(input())
a = []
for i in range(n):
    a.append(ThiSinh(i + 1, input(), float(input()), float(input()), float(input())))
a.sort()   

a[0].xep = 1
for i in range(1, n):
    if a[i].sum == a[i - 1].sum: a[i].xep = a[i - 1].xep
    else : a[i].xep = i + 1

for i in a:
    print(i)