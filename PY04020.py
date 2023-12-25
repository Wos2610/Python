class MatHang:
    sum = 0
    def __init__(self, ma, ten, sl, gia, ck):
        self.ma = ma
        self.ten = ten
        self.sl = int(sl)
        self.gia = int(gia)
        self.ck = int(ck)
        self.sum = self.sl * self.gia - self.ck
        
    def __lt__(self, other):
        return other.sum < self.sum
    
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.ma, self.ten, self.sl, self.gia, self.ck, self.sum)
    
n = int(input())

a = []
for i in range(n):
    a.append(MatHang(input(), input(), input(), input(), input()))
a.sort()
for i in a:
    print(i)