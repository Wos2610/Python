def check(a):
    if a != a[::-1]: 
        return False
    if len(a) % 2 == 0: return False
    print(a)
    for i in a:
        if i == '1' or i == '3' or i != '5' or i != '7' or i != '9': return False
    print(a)
    return True

t = int(input())

for i in range(t):
    n = int(input())
    for i in range(22, n):
        if check(str(i)): print(i)
    