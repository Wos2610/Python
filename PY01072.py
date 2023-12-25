a = [0] * 106
b = [0] * 1006
def Try(i, k, n):
    if i == k + 1:
        for j in range(1, k + 1):
            print(b[a[j] - 1], end=" ")
        print()
        return

    for j in range(a[i - 1] + 1, n - k + i + 1):
        a[i] = j
        Try(i + 1, k, n)
        
n, k = input().split()
n = int(n)
k = int(k)

arr = input()
b = list(map(int, arr.split()))
b = sorted(set(b))

n = len(b)
    
Try(1, k, n)
        

        