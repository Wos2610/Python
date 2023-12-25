def gcd(a, b):
    temp = 0
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return a


n, k = input().split()
k = int(k)
n = int(n)
begin = 10 ** (k - 1)
end = 10 ** k
d = 0
for i in range(begin, end):
    if(gcd(i, n) == 1): 
        print(i, end = ' ')
        d += 1
        if(d == 10): 
            print("\n")
            d = 0
    