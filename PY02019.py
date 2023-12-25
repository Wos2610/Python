def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b 
        b = tmp
    return a

n = int(input())

a = [int(x) for x in input().split()]
a = sorted(a)
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j], end=' ')
            print()