def check(a):
    for i in range(len(a) - 2):
        if a[i] != a[i + 2]: return False
    return True

t = int(input())
for i in range(t):
    n = input()
    if check(n) == True: print("YES")
    else: print("NO")
