class Mon:
    def __init__(self, ma, ten, tin, lt, th):
        self.ma = ma
        self.ten = ten
        self.tin = int(tin)
        self.lt = lt
        self.th = th
        
    def __lt__(self, other):
        return self.ma < other.ma
    
    def __str__(self):
        return '{} {} {} {} {}'.format(self.ma, self.ten, str(self.tin), self.lt, self.th)
        
f = open('MONHOC.in', 'r')
n = int(f.readline())
a = []
for i in range(n):
    a.append(Mon(f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()))
    
a.sort()

for i in a:
    print(i.th[16:])
    if i.th == "Truc tuyen" or i.th.endswith("code.ptit.edu.vn"):
        print(i)
    