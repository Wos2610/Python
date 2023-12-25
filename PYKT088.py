import math
def check(m):
    res = 1
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            d = 0
            while m % i == 0:
                m //= i
                d += 1
            res *= (d + 1)
            if res > 9: return False
        if m == 1: break
    
    if m > 1: res *= 2      
    if res == 9: return True
    else: return False
               
n = int(input())
d = 0
for i in range(1, n + 1):
    if check(i): d += 1
print(d)
    