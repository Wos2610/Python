import re
def check(s):
    a = re.split('[.]', s)
    if len(a) != 4: return False
    for i in a:
        try:
            tmp = int(i)
            if tmp < 0 or tmp > 255: return False
        except:
            return False
    return True

t = int(input())
for i in range(t):
    s = input()
    if check(s): print("YES")
    else: print("NO")