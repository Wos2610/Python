def check(a):
    for i in range(len(a)):
        if a[i] != "0" and a[i] != "1" and a[i] != "2": return False
    return True

t = int(input())
while(t > 0):
    t -= 1
    s = input()
    if(check(s) == True): print("YES")
    else: print("NO")