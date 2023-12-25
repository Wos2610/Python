import pickle
def check(v):
    s = str(v)
    if len(s) < 2: return False
    for i in range(1, len(s)):
        if s[i] < s[i - 1]: return False
    return True

class Number:
    def __init__(self, x, a1, a2):
        self.x = x
        self.a1 = a1
        self.a2 = a2
    
    def __lt__(self, other):
        return self.x < other.x
    
    def __str__(self):
        return '{} {} {}'.format(self.x, self.a1, self.a2)
# d = [59, 2, 66, 423, 59]
# f = open('DATA1.in', 'wb')
# pickle.dump(d, f)

# e = [59, 66, 66, 48, 42]
# f = open('DATA2.in', 'wb')
# pickle.dump(e, f)
   
with open('DATA1.in', 'rb') as f:
    b = pickle.load(f)
with open('DATA2.in', 'rb') as f:
    c = pickle.load(f)
a = []

for i in b:
    if check(i):
        m = 0
        for j in a:
            if j.x == i:
                j.a1 += 1
                m = 1
                break
        if m == 0:
            a.append(Number(i, 1, 0))

for i in c:
    if check(i):
        m = 0
        for j in a:
            if j.x == i:
                j.a2 += 1
                m = 1
                break 
        if m == 0:
            a.append(Number(i, 0, 1))
            
for i in a:
    if i.a1 > 0 and i.a2 > 0:
        print(i)
