def check(s):
    if len(s) < 3: return False
    l = -1
    r = len(s)
    for i in range(1, len(s)):
        if s[i] > s[i - 1]:
            l = i
        else: break
    
    for i in range(len(s) - 2, -1, -1):
        if s[i] > s[i + 1]:
            r = i
        else: break
    
    if l == r: return True
    return False

t = int(input())
for i in range(t):
    s = input()
    if check(s): print("YES")
    else: print("NO")
        