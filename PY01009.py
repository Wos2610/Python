def isUpperString(a):
    l = 0
    u = 0
    for i in a:
        if i >= 'A' and i <= 'Z': u += 1
        else: l += 1
    if u > l: return True
    return False
    
s = input()

if isUpperString(s): print(s.upper())
else: print(s.lower())