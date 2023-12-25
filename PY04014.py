from decimal import ROUND_HALF_UP, Decimal
class Student:
    ma = ""
    sum = 0
    loai = ""
    def __init__(self, id, name, x):
        self.ma = 'HS{:02d}'.format(id)
        self.name = name
        self.tinh(x)
        
    def tinh(self, x):
        for i in range(0, 2):
            self.sum += x[i] * 2
        for i in range(2, 10):
            self.sum += x[i]
        
        self.sum /= 12
        
        self.sum = round((self.sum + 0.005) * 10) / 10
        if self.sum >= 9: self.loai = "XUAT SAC"
        elif self.sum >= 8: self.loai = "GIOI"
        elif self.sum >= 7: self.loai = "KHA"
        elif self.sum >= 5: self.loai = "TB"
        else: self.loai = "YEU"
        
    def __lt__(self, other):
        if self.sum == other.sum:
            return self.ma < other.ma
        return self.sum > other.sum
    
    def __str__(self):
        return '{} {} {:.1f} {}'.format(self.ma, self.name, self.sum, self.loai)
    
n = int(input())
a = []
for i  in range(n):
    name = input().strip()
    x = [float(x) for x in input().strip().split()]
    a.append(Student(i+1, name, x))
a.sort()
for i in a:
    print(i)