class Xe :
    def __init__(self, bienSo, type, num, huong, date):
        self.bienSo = bienSo
        self.type = type
        self.num = num
        self.huong = huong
        self.date = date
        self.sum = 0
    
    def tinh(self):
        if self.huong == "IN":
            if self.type == "Xe_con":
                if self.num == 5: self.sum = 10000
                if self.num == 7: self.sum = 15000
            if self.type == "Xe_tai":
                if self.num == 2: self.sum = 20000
            if self.type == "Xe_khach":
                if self.num == 29: self.sum = 50000
                if self.num == 45: self.sum = 70000

n = int(input())
a = []
c = {}
while n > 0:
    n -= 1
    b = input().split()
    x = Xe(b[0], b[1], int(b[2]), b[3], b[4])
    x.tinh()
    if x.date in c:
        c[x.date] += x.sum
    else:
        c[x.date] = x.sum

for i in c:
    print(i + ": " + str(c[i]))
    
    

