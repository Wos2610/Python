m = [0] * 1000006
save = []
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 1000006):
        if m[i] == 0:
            for j in range(i * i, 1000006, i):
                m[j] = i
    
    for i in range(2, 1000006):
        if m[i] == 0:
            save.append(i)
            
sieve()
n, x = input().split()
n = int(n)
x = int(x)

for i in range(0, n + 1):
    print(x, end = " ")
    x += save[i]
    