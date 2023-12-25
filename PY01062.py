m = [0] * 100006
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 100006):
        if m[i] == 0:
            for j in range(i * i, 100006, i):
                m[j] = i

def check(s):
    n = len(s)
    if m[n] != 0: return False
    
    d = 0
    for i in s:
        if i == '2' or i == '3' or i == '5' or i == '7': d += 1
    if d <= n - d: return False
    return True
    

sieve()
t = int(input())
while(t > 0):
    t -= 1
    s = input()
    if(check(s) == True): print("YES")
    else: print("NO")