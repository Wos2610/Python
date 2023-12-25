from datetime import datetime
class SinhVien:
    sum = 0
    def __init__(self, name, start, end):
        self.name = name
        formatter = '%d/%m/%Y %H:%M:%S'
        self.start = datetime.strptime(start, formatter)
        self.end = datetime.strptime(end, formatter)
        self.tinh()
        
    def tinh(self):
        self.sum = (self.end - self.start).total_seconds() / 60
        
    def __lt__(self, other):
        if self.sum == other.sum:
            return self.name < other.name
        return self.sum > other.sum
    
    def __str__(self):
        return '{} {:.0f}'.format(self.name, self.sum)
    
f = open('ONLINE.in', 'r')
n = int(f.readline())
a = []
for i in range(n):
    a.append(SinhVien(f.readline().strip(), f.readline().strip(), f.readline().strip()))
    
a.sort()
for i in a:
    print(i)
        