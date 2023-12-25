class Student:
    diemDanh = ""
    diem = 10
    
    def __init__(self, ma, name, lop):
        self.ma = ma
        self.name = name
        self.lop = lop
        
        
    def tinh(self):
        for i in range(10):
            if self.diemDanh[i] == "m":
                self.diem -= 1
            elif self.diemDanh[i] == "v":
                self.diem -= 2
        if self.diem < 0:
            self.diem = 0
            
    def __str__(self):
        res = self.ma + " " + self.name + " " + self.lop + " " + str(self.diem)
        if self.diem == 0:
            res += " " + "KDDK"
        return res

n = int(input())
a = []

for i in range(n):
    a.append(Student(input(), input(), input()))
    
for i in range(n):
    ma, dd = input().split()
    for j in a:
        if j.ma == ma:
            j.diemDanh = dd

for i in a:
    i.tinh()
    print(i)
    
    
    