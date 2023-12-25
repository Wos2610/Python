from datetime import datetime
class Mon:
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten

class Ca:
    date = ""
    def __init__(self, ma, mon, day, time, nhom):
        self.ma = 'T{:03d}'.format(ma)
        self.mon = mon
        self.day = day
        self.time = time
        self.date = datetime.strptime(day + " " + time, '%d/%m/%Y %H:%M')
        self.nhom = nhom
    
    def __lt__(self, other):
        if self.date == other.date:
            return self.ma < other.ma
        return self.date < other.date
    
    def __str__(self):
        return self.ma + " " + self.mon.ma + " " + self.mon.ten + " " + self.day + " " + self.time + " " + self.nhom

n, m = list(map(int, input().split()))

a = []
for i in range(n):
    a.append(Mon(input().strip(), input().strip()))

b = []
for i in range(m):
    tmp = input().strip().split()
    mon = None
    for j in a:
        if j.ma == tmp[0]:
            mon = j
            break
    b.append(Ca(i + 1, mon, tmp[1], tmp[2], tmp[3]))
    
b.sort()
for i in b:
    print(i)