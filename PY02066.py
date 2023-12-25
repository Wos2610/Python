n = int(input())

a = []
d = 0
while len(a) < n:
    a += list(map(int, input().split()))
    
if a[0] != 1:
    for i in range(1, a[0]):
        print(i)
    d = 1
    
for i in range(1, n):
    while a[i] != a[i - 1] + 1:
        a[i - 1] += 1
        print(a[i - 1])
        d = 1

if d == 0:
    print("Excellent!")