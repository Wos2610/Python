import re
n = int(input())

a = []

class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, other):
        if self.value == other.value:
            return self.key < other.key
        return self.value > other.value
    
    def __str__(self):
        return '{} {}'.format(self.key, self.value)

for i in range(n):
    b = re.split("[^a-z0-9]", input().lower())
    for j in b:
        if j != "":
            m = 0
            for k in a:
                if k.key == j:
                    k.value += 1
                    m = 1
                    break
            if m == 0: a.append(Pair(j, 1))

a.sort()
for i in a:
    print(i)
