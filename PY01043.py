n = 0
m = 0
a = [0] * 100
b = ['0', '2', '4', '6', '8']
def Try(i, n):
    if i == n + 1:
        temp = ""
        for j in range(1, n + 1):
            temp += a[j]
        for j in range(n, 0, -1):
            temp += a[j]
        if int(temp) < m: print(temp, end = ' ')
        return
    for j in range(len(b)):
        if i == 1 and j == 0: continue
        a[i] = b[j]
        Try(i + 1, n)
        
t = int(input())
while(t > 0):
    t -= 1
    m = int(input())
    for i in range(1, 4):
        Try(1, i)
    print()
    