m = [0] * 1000000

def sieve():
    m[0] = m[1] = 1
    for i in range(2, 1000000):
        if m[i] == 0:
            for j in range(i * i, 1000000, i):
                m[j] = i

def check(s):
    k = len(s)
    sum = 0
    for i in range(k):
        sum += int(s[i])
    if m[sum] == 0: return True
    return False

sieve()               
t = int(input())
while t > 0:
    t -= 1
    n = input()
    if check(n) == True: print("YES")
    else: print("NO")
    