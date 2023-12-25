n = int(input())
a = list(map(int, input().split()))

a.sort()
res = a[n - 1] * a[n - 2]
res = max(res, a[0] * a[1])
res = max(res, a[0] * a[1] * a[n - 1])
res = max(res, a[n - 1] * a[n - 2] * a[n - 3])

print(res)