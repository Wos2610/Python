class Tu:
    def __init__(self, s, x, y):
        self.s = s
        self.x = x
        self.y = y
        
    def __lt__(self, other):
        return self.s < other.s 
    
    def __str__(self):
        return self.s

a = []   
s1 = input().split()
s2 = input().split()

for i in s1:
    i = i.lower()
    m = 0
    for j in a:
        if j.s == i:
            j.x += 1
            m = 1
            break
    if m == 0: a.append(Tu(i, 1, 0))
    
for i in s2:
    i = i.lower()
    m = 0
    for j in a:
        if j.s == i:
            j.y += 1
            m = 1
            break
    if m == 0: a.append(Tu(i, 0, 1))
    
a.sort()
for i in a:
    print(i, end = " ")
print()

for i in a:
    if i.x > 0 and i.y > 0:
        print(i, end = " ")
        

        

