m = [0] * 100001
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 100001):
        if m[i] == 0:
            for j in range(i * i, 100001, i):
                m[j] = i
    
def check(s):
    n = len(s)
    sum = 0
    for i in range(0, n, 2):
        if int(s[i]) % 2 == 1: return False
        sum += int(s[i])
    for i in range(1, n, 2):
        if int(s[i]) % 2 == 0: return False   
        sum += int(s[i])
    if m[sum] != 0: return False
    return True

t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check(s) == True: print("YES")
    else: print("NO")