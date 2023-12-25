t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    print("Test %d:" %(i+1), end = " ")
    if s1 == s2: print("YES")   
    else: print("NO")