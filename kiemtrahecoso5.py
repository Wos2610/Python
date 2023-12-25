def check(s):
    sum = 0
    for i in range(len(s)):
        if s[i] != '0' and s[i] != '1' and s[i] != '2' and s[i] != '3' and s[i] != '5':
            return False
        sum += ord(s[i]) - ord('0')
    if sum == 5: return True
    return False

t = int(input())
for i in range(t):
    s = input()
    if check(s): print("YES")
    else: print("NO")