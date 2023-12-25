a = []

while len(a) < 10:
    arr = list(map(int, input().split()))
    
    for i in arr:
        a.append(i)

m = [0] * 50
for i in range(0, 10):
    m[a[i] % 42] = 1

d = 0    
for i in m:
    if i != 0: d += 1
print(d)