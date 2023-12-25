a = [0] * 20
b = [2, 3, 5]
m = {1 : 1}
d = 0
def Try(i, n):
    if i == n + 1:
        res = 1
        for j in range(1, n + 1):
            res *= a[j]
        if m.get(res) == 0:
            d += 1
            m = d
        return
    
    for j in b:
        a[i] = j
        Try(i + 1, n)
        
def Tinh():
    for i in range(1, 10):
        Try(1, i)
        
t = int(input())
Tinh()

while t > 0:
    t -= 1
    n = int(input())
    d = 0
    if m.get(n) != 0: print(m.get(n))
    else: print("Not in sequence")

            