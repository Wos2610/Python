m = [0] * 1000006
         
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 1000006):
        if m[i] == 0:
            for j in range(i * i, 1000006, i):
                m[j] = i

n, k = input().split()
n = int(n)
k = int(k)

sieve()

for i in range(n):
    a = [int(x) for x in input().split()]
    for i in a:
        if m[i] == 0: print(1, end=' ')
        else: print(0, end=' ')
    print()


