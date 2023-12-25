b = [0] * 36
n, k = list(map(int, input().split()))
a = []

a = input().split()
a = list(set(a))
a.sort()
   
def Try(i, k, n):
    if i == k + 1:
        for j in range(1, k + 1):
            print(a[b[j] - 1], end = " ")
        print()
        return
    for j in range(b[i - 1] + 1, n - k + i + 1):
        b[i] = j
        Try(i + 1, k, n)
        
Try(1, k, len(a))


    
