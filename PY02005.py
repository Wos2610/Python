n = int(input())

arr = input()
a = list(map(int, arr.split()))
d = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            d += 1
print(d)