def check(s):
    n = len(s)
    d = 0
    for i in range(n):
        if s[i] != '6' and s[i] != '8': 
            return False
        else:
            if s[i] == '8': d += 1
            else: d = 0
            if d == 3: return False
    return True

s = input()
if check(s): print("YES")
else: print("NO")
