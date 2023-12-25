m = [0] * 1000

def sieve():
    m[0] = m[1] = 1
    for i in range(2, 1000):
        if m[i] == 0:
            for j in range(i * i, 1000, i):
                m[j] = i
                
b = {'2', '3', '5', '7'}
           
def check(s):
    n = len(s)
    if m[n] != 0: return False
    primes = 0
    for i in s:
        for j in b:
            if i == j:
                primes += 1
                break
    if(primes <= n - primes): return False
    return True
               
t = int(input())
sieve()
while(t > 0):
    t -= 1
    s = input()
    if check(s) == True: print("YES")
    else: print("NO")
        
                
