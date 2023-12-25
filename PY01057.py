m = [0] * 100001
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 100001):
        if m[i] == 0:
            for j in range(i * i, 100001, i):
                m[j] = i
    
def check(s):
    n = len(s)
    for i in range(0, n):
        if m[i] == 0 and m[int(s[i])] != 0: return False
        if m[i] != 0 and m[int(s[i])] == 0: return False
    return True

sieve()
t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check(s) == True: print("YES")
    else: print("NO")