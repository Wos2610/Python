t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()
    
    a = []
    for j in s1:
        a.extend(j)
        
    b = []
    for j in s2:
        b.extend(j)

    a.sort()
    b.sort()

    print("Test {}:".format(str(i + 1)), end = " ")
    if a == b: print("YES")
    else: print("NO")