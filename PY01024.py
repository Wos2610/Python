def check(s):
    n = len(s)
    sum = int(s[0])
    for i in range(1, n):
        sum += int(s[i])
        if abs(ord(s[i]) - ord(s[i - 1])) != 2:
            return False
    if sum % 10 != 0: return False
    return True

t = int(input())
while t > 0:
    t -= 1
    s = input()
    if check(s): print("YES")
    else: print("NO")
        
    