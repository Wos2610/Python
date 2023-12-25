def gcd(a, b):
    temp = 0
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

l, r = input().split()
l = int(l)
r = int(r)

for i in range(l, r - 1):
    for j in range(i + 1, r):
        for k in range(j + 1, r + 1):
            if gcd(i, j) == 1 and gcd(i, k) == 1 and gcd(j, k) == 1: 
                print(f"({i}, {j}, {k})")
