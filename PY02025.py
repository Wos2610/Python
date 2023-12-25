class Num:
    def __init__(self, s, x, y):
        self.s = s
        self.x = x
        self.y = y
    def __lt__(self, other):
        return self.s < other.s
    def __str__(self):
        return str(self.s)
            
n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in a:
    mark = 0
    for j in c:
        if j.s == i:
            j.x += 1
            mark = 1
            break
    if mark == 0: c.append(Num(i, 1, 0))

for i in b:
    mark = 0
    for j in c:
        if j.s == i:
            j.y += 1
            mark = 1
            break
    if mark == 0: c.append(Num(i, 0, 1))

c.sort()
for i in c:
    if i.x > 0 and i.y > 0:
        print(i, end = " ")
print()
for i in c:
    if i.x > 0 and i.y == 0:
        print(i, end = " ")
print()       
for i in c:
    if i.x == 0 and i.y > 0:
        print(i, end = " ")
