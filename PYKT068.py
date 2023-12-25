class Mon:
    def __init__(self, ma, ten, hinhThuc):
        self.ma = ma
        self.ten = ten
        self.hinhThuc = hinhThuc
    
    def __lt__(self, other):
        return self.ma < other.ma
    
    def __str__(self):
        return "{} {} {}".format(self.ma, self.ten, self.hinhThuc)
    
n = int(input())
a = []
for i in range(n):
    a.append(Mon(input(), input(), input()))

a.sort()
for i in a:
    print(i)