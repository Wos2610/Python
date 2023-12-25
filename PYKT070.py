from datetime import datetime
class Mon:
    def __init__(self, ma, name, type):
        self.ma = ma
        self.name = name
        self.type = type
    
class Ca:
    date = ""
    def __init__(self, id, day, time, room):
        self.ma = 'C{:03d}'.format(id)
        self.day = day
        self.time = time
        self.date = datetime.strptime(day + " " + time, '%d/%m/%Y %H:%M')
        self.room = room

class Lich:
    def __init__(self, ca, mon, nhom, sl):
        self.ca = ca
        self.mon = mon
        self.nhom = nhom
        self.sl = sl
        
    def __lt__(self, other):
        if self.ca.date == other.ca.date:
            return self.ca.ma < other.ca.ma
        return self.ca.date < other.ca.date

    def __str__(self):
        return self.ca.day + " " + self.ca.time + " " + self.ca.room + " " + self.mon.name + " " + self.nhom + " " + self.sl
    
f = open('MONTHI.in', 'r')
n = int(f.readline())
a = []
for i  in range(n):
    a.append(Mon(f.readline().strip(), f.readline().strip(), f.readline().strip()))
    
f = open('CATHI.in', 'r')
m = int(f.readline())
b = []
for i in range(m):
    b.append(Ca(i+1, f.readline().strip(), f.readline().strip(), f.readline().strip()))
    
f = open('LICHTHI.in', 'r')
k = int(f.readline())
c = []
for i in range(k):
    tmp = f.readline().strip().split()
    ca = None
    mon = None
    for j in b:
        if j.ma == tmp[0]:
            ca = j
            break
    for j in a:
        if j.ma == tmp[1]:
            mon = j
            break
    c.append(Lich(ca, mon, tmp[2], tmp[3]))

c.sort()
for i in c:
    print(i)