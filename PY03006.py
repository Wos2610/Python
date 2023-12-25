import re
def check(s):
    for i in s:
        if i in '0123456789': return False
        
    return True
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
    
n = int(input())
a = []
for i in range(n):
    b = re.split('[^a-z]', input().lower())
    for j in b:
        if j != "" and check(j):
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
    print(i)

