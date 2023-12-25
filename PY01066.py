def check(s):
    s0 = s[::-1]
    n = len(s)
    for i in range(1, n):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s0[i]) - ord(s0[i - 1])) : return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    s = input()
    if(check(s) == True): print("YES")
    else: print("NO")