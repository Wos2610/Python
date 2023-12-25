class Khach:
    ma = ""
    sum = 0
    bonus = 0
    def __init__(self, id, name, cu, moi):
        self.ma = 'KH{:02d}'.format(id)
        self.name = name
        self.cu = cu
        self.moi = moi
        self.tinh()
    
    def tinh(self):
        tmp = self.moi - self.cu
        bonus = 0
        if tmp <= 50: bonus = 102 / 100
        elif tmp <= 100: bonus = 103 / 100
        else: bonus = 105 / 100
        
        if tmp <= 50:
            self.sum = tmp * 100
        elif tmp <= 100:
            self.sum = 50 * 100 + (tmp - 50) * 150
        else:
            self.sum = 50 * 100 + 50 * 150 + (tmp - 50 - 50) * 200
        
        self.sum *= bonus 
        
    def __lt__(self, other):
        return self.sum > other.sum
    
    def __str__(self):
        return '{} {} {}'.format(self.ma, self.name, round(self.sum))
    
n = int(input())
a = []
for i in range(n):
    a.append(Khach(i+1, input(), int(input()), int(input())))
a.sort()
for i in a:
    print(i)
    