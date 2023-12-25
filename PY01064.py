a = [0] * 100

a[1] = 1
for i in range(2, 100):
    a[i] = a[i - 1] * 2 + 1

def Try(n, k):
    if k == a[n] // 2 + 1: return n
    elif k > a[n] // 2 + 1: return Try(n - 1, k - a[n] // 2 - 1)
    else: return Try(n - 1, k)
  
t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    print(chr(Try(n, k) + 64))


    