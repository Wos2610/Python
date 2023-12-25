class Mon:
    def __init__(self, ma, ten, tin):
        self.ma = ma
        self.ten = ten
        self.tin = tin
        
class Lich:
    ma = ""
    def __init__(self, id, mon, thu, kip, gv, room):
        self.ma = 'HP{:03d}'.format(id)
        self.mon = mon
        self.thu = thu
        self.kip = kip
        self.gv = gv
        self.room = room
    
    def __lt__(self, other):
        if self.thu == other.thu:
            if self.kip == other.kip:
                return self.gv < other.gv
            return self.kip < other.kip
        return self.thu < other.thu
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma, self.thu, self.kip, self.gv, self.room)
    
f = open('MONHOC.in', 'r')
n = int(f.readline())
a = []
for i in range(n):
    a.append(Mon(f.readline().strip(), f.readline().strip(), int(f.readline().strip())))

f = open('LICHGD.in', 'r')
m = int(f.readline())
b = []
for i in range(m):
    maMon = f.readline().strip()
    mon = None
    for j in a:
        if j.ma == maMon:
            mon = j
            break
    b.append(Lich(i + 1, mon, f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()))
b.sort()    
x = f.readline()
m = 0
for i in b:
    if i.mon.ma == x:
        if m == 0:
            print('LICH GIANG DAY MON {}:'.format(i.mon.ten))
            m = 1
        print(i)
