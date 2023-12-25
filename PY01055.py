def check(s):
    n = len(s)
    if n % 2 == 0: return False
    if s[0] == s[1]: return False
    for i in range(2, n, 2):
        if s[i] != s[i - 2]: return False
    return True

t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check(s) == True: print("YES")
    else: print("NO")