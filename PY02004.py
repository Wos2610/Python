n = int(input())

arr = input()
a = list(map(int, arr.split()))

d = 0
for i in range(1, n):
    if a[i] != a[i - 1]: d += 1
print(d)
    