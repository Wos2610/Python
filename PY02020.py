n = int(input())

a = [float(x) for x in input().split()]
a = sorted(a)
l, r = 0, 0
for i in range(1, n):
    if a[i] != a[i - 1]:
        l = i
        break
        
for i in range(n - 2, -1, -1):
    if a[i] != a[i + 1]:
        r = i
        break

sum = 0
for i in range(l, r + 1):
    sum += a[i]
sum /= (r - l + 1)
print('%.2f' %sum)
        

