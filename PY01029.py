def gcd(a, b):
    temp = 0
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return a

t = int(input())
for i in range(t) : 
    n = int(input())
    m = n
    temp = 0
    while m > 0:
        temp = temp * 10 + m % 10
        m = int(m / 10)
       
    if(gcd(temp, n) == 1): print("YES")
    else: print("NO")
    