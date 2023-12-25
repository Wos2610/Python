import math
m = [0] * 2000006
primes = []
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 2000006):
        if m[i] == 0:
            for j in range(i * i, 2000006, i):
                m[j] = i
    for i in range(2, 2000006):           
        if m[i] == 0: m[i] = i
            
n = int(input())
sieve()
res = 0
while n > 0:
    n -= 1
    k = int(input())
    
    while k % m[k] == 0 and k > 1:
        res += m[k]
        k //= m[k]
        
    
print(res)
            