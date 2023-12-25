class SinhVien:
    def __init__(self, ma, ten, phone, mail):
        self.ma = ma
        self.ten = ten
        self.phone = phone
        self.mail = mail
        
class DeTai:
    def __init__(self, id, ten, de):
        self.ma = 'DT{:03d}'.format(id)
        self.ten = ten
        self.de = de
        
class HoiDong:
    def __init__(self, sv, dt, hd):
        self.sv = sv
        self.dt = dt
        self.hd = hd
    
    def __lt__(self, other):
        return self.sv.ma < other.sv.ma
    
    def __str__(self):
        return '{} {} {} {}'.format(self.sv.ma, self.sv.ten, self.dt.de, self.dt.ten)
    
f = open('SINHVIEN.in', 'r')
n = int(f.readline())
a = []
for i in range(n):
    a.append(SinhVien(f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()))

f = open('DETAI.in', 'r')
m = int(f.readline())
b = []
for i in range(m):
    b.append(DeTai(i + 1, f.readline().strip(), f.readline().strip()))
    
f = open('HOIDONG.in', 'r')
k = int(f.readline())
c = []
for i in range(k):
    sv = None
    dt = None
    hd = None
    p = f.readline().strip().split()
    for j in a:
        if j.ma == p[0]:
            sv = j
            break
    for j in b:
        if j.ma == p[1]:
            dt = j
            break
    c.append(HoiDong(sv, dt, p[2]))
    
c.sort()
for i in range(1, 9):
    m = 0
    for j in c:
        if j.hd[2] == str(i):
            if m == 0:
                print("DANH SACH HOI DONG {}:".format(i))
                m = 1
            print(j)
    