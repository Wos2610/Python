class ThiSinh:
    ma = ""
    bonus = 0
    sum = 0
    status = ""
    def __init__(self, id, ten, diem, danToc, khuVuc):
        self.ma = "TS{:02d}".format(id)
        self.ten = ten
        self.diem = float(diem)
        self.danToc = danToc
        self.khuVuc = khuVuc
        self.tinh()
        
    def chuanHoaTen(self, s):
        a = s.strip().split()
        res = ""
        for i in range(len(a)):
            res += a[i][:1].upper() + a[i][1:].lower()
            if i != len(a) - 1: res += " "
        return res

    def tinh(self):
        self.ten = self.chuanHoaTen(self.ten)
        
        if self.khuVuc == "1": bonus = 1.5
        elif self.khuVuc == "2": bonus = 1
        elif self.khuVuc == "3": bonus = 0
        
        if self.danToc == "Kinh": bonus += 0
        else: bonus += 1.5
        
        self.sum = self.diem + bonus
        if self.sum >= 20.5: self.status = "Do"
        else: self.status = "Truot"
        
    def __lt__(self, other):
        if self.sum == other.sum:
            return self.ma < other.ma
        return self.sum > other.sum
    
    def __str__(self):
        return "{} {} {:.1f} {}".format(self.ma, self.ten, self.sum, self.status)
    
n = int(input())
a = []
for i in range(n):
    a.append(ThiSinh(i + 1, input(), input(), input(), input()))
    
a.sort()
for i in a:
    print(i)

    
            