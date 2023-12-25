import re
class Num:
    def __init__(self, s, x):
        self.s = s
        self.x = x
    
    def __lt__(self, other):
        if self.x == other.x:
            return self.s < other.s 
        return self.x > other.x
    
    def __str__(self):
        return '{} {}'.format(self.s, self.x)
    
n, k = list(map(int, input().split()))
a = []
for i in range(n):
    b = re.split('[^0-9a-z]', input().lower())
    for j in b:
        if j != "":
            mark = 0
            for l in a:
                if l.s == j:
                    l.x += 1
                    mark = 1
                    break
            if mark == 0:
                a.append(Num(j, 1))

a.sort()
for i in a:
    if i.x >= k:
        print(i)

