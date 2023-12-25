from datetime import datetime
class Khach:
    sum = 0
    day = 0
    
    def __init__(self, id, ten, phong, start, end, bonus):
        self.ma = 'KH{:02d}'.format(id)
        self.ten = ten.strip()
        self.phong = phong.strip()
        formatter = '%d/%m/%Y'
        self.start = datetime.strptime(start.strip(), formatter)
        self.end = datetime.strptime(end.strip(), formatter)
        self.bonus = int(bonus)
        self.tinh()
        
    def tinh(self):
        self.day = (self.end - self.start).days + 1
        donGia = 0
        if self.phong[0] == '1': donGia = 25
        elif self.phong[0] == '2': donGia = 34
        elif self.phong[0] == '3': donGia = 50
        else: donGia = 80
        
        self.sum = donGia * self.day + self.bonus
    
    def __lt__(self, other):
        return self.sum > other.sum    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma, self.ten, self.phong, self.day, self.sum)
    
n = int(input())
a = []
for i in range(n):
    a.append(Khach(i + 1, input(), input(), input(), input(), input()))

a.sort()
for i in a:
    print(i)