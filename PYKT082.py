class Diem:
    r, l, s, w, sum = 0, 0, 0, 0, 0
    def __init__(self, x, y, s, w):
        self.r = self.tinh(x)
        self.l = self.tinh(y)
        self.s = s
        self.w = w
        self.tinhDiem()
        
    def tinh(self, x):
        if x >= 39 and x <= 40:
            return 9
        elif x >= 37 and x <= 38:
            return 8.5
        elif x >= 35 and x <= 36:
            return 8
        elif x >= 33 and x <= 34:
            return 7.5
        elif x >= 30 and x <= 32:
            return 7
        elif x >= 27 and x <= 29:
            return 6.5
        elif x >= 23 and x <= 26:
            return 6
        elif x >= 20 and x <= 22:
            return 5.5
        elif x >= 16 and x <= 19:
            return 5
        elif x >= 13 and x <= 15:
            return 4.5
        elif x >= 10 and x <= 12:
            return 4
        elif x >= 7 and x <= 9:
            return 3.5
        elif x >= 5 and x <= 6:
            return 3
        elif x >= 3 and x <= 4:
            return 2.5
        
    def tinhDiem(self):
        self.sum = (self.l + self.r + self.s + self.w) / 4
        if self.sum - int(self.sum) >= 0.75:
            self.sum = int(self.sum) + 1.0
        elif self.sum - int(self.sum) >= 0.25:
            self.sum = int(self.sum) + 0.5
        else:
            self.sum = int(self.sum)
    
    def __str__(self):
        return str(self.sum)
    
n = int(input())
a = []
for i in range(n):
    x, y, s, w = map(float, input().split())
    a.append(Diem(int(x), int(y), s, w))
    
for i in a:
    print(i)