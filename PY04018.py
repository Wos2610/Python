class Nguoi:
    id = ""
    mon = ""
    diem = 0
    status = ""
    bonus = 0
    
    def __init__(self, id, ten, ma, tin, chuyen):
        self.id = "GV{:02d}".format(id)
        self.ten = ten
        self.ma = ma
        self.tin = float(tin)
        self.chuyen = float(chuyen)
        
    def tinh(self):
        if self.ma[0] == 'A':
            self.mon = "TOAN"
        elif self.ma[0] == 'B':
            self.mon = "LY"
        elif self.ma[0] == 'C':
            self.mon = "HOA"
            
        if self.ma[1] == '1':
            self.uuTien = 2
        elif self.ma[1] == '2':
            self.uuTien = 1.5
        elif self.ma[1] == '3':
            self.uuTien = 1
        else: self.uuTien = 0

        self.diem = self.tin * 2 + self.chuyen + self.uuTien
        
        if self.diem >= 18: self.status = "TRUNG TUYEN"
        else : self.status = "LOAI"
        
    def __lt__(self, other):
        return other.diem < self.diem
        
    def __str__(self):
        return "{} {} {} {:.1f} {}".format(self.id, self.ten, self.mon, self.diem, self.status)
    
n = int(input())
a = []
for i in range(n):
    a.append(Nguoi(i + 1, input(), input(), input(), input()))

for i in a:
    i.tinh()

a.sort()

for i in a:
    print(i)