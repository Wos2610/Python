import math

def tinh(a, b, c, d, e, f):
        ab = math.sqrt((c - a) ** 2 + (d - b) ** 2)
        bc = math.sqrt((e - c) ** 2 + (f - d) ** 2)
        ac = math.sqrt((e - a) ** 2 + (f - b) ** 2)
        
        if ab + bc <= ac or ab + ac <= bc or bc + ac <= ab:
            return -1
        else:
            return ab + bc + ac
        
class Tam:
    cv = 0
    def __init__(self, a, b, c, d, e, f):
        self.cv = tinh(a, b, c, d, e, f)
        
    def __str__(self):
        if self.cv == -1:
            return "INVALID"
        else:
            return '{:.3f}'.format(self.cv)

t = int(input())
a = []
while True:
    try:
        a += list(map(float, input().split()))
    except:
        break
i = 0
for j in range(t):  
    print(Tam(a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4], a[i + 5]))
    i += 6
