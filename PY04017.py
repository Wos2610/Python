from datetime import datetime
class Nguoi:
    ma = ""
    v = 0
    def __init__(self, ten, dv, time):
        self.ten = ten
        self.dv = dv
        self.time = datetime.strptime("0" + time, '%H:%M')
        self.tinh()
    def tinh(self):
        a = self.dv.split()
        for i in a:
            self.ma += i[:1].upper()
        b = self.ten.split()
        for i in b:
            self.ma += i[:1].upper()
        
        start = datetime.strptime("06:00", '%H:%M')
        t = (self.time - start).seconds / 3600
        self.v = 120 / t
        
    def __lt__(self, other):
        return self.v > other.v
        
    def __str__(self):
        return '{} {} {} {} Km/h'.format(self.ma, self.ten, self.dv, round(self.v))
    
n = int(input())
a = []
for i in range(n):
    a.append(Nguoi(input(), input(), input()))

a.sort()
for i in a:
    print(i)