m = [0] * 100006
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 100006):
        if m[i] == 0:
            for j in range(i * i, 100006, i):
                m[j] = i
                
def check(s):
    s0 = s[-4::]  
    if m[int(s0)] == 0: return True
    return False

t = int(input())
sieve()
while(t > 0):
    t -= 1
    s = input()
    if(check(s) == True): print("YES")
    else: print("NO")