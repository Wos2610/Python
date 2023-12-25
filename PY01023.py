import math
m = [0] * 1000006

def sieve():
    m[0] = m[1] = 1
    for i in range(2, 1000006):
        if m[i] == 0:
            for j in range(i * i, 1000006, i):
                m[j] = i

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    
    print(f"1", end = '')
    if n > 1: print(" * ", end = '')
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d = 0
            while(n % i == 0):
                d += 1
                n //= i
            print(f"{i}^{d}", end = '')
            if n > 1: print(" * ", end = '')
    
    if n > 1: print(f"{n}^1", end = '')
    print()
                