a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def tinh(n, b):
    res = ""
    while True:
        k = n // b
        d = n % b
        res += a[d]
        if k == 0: break
        n = k
    return res[::-1]
        
t = int(input())
for i in range(t):
    n, b = list(map(int, input().split()))
    print(tinh(n, b))
    

    
    