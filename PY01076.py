def gcd(a, b):
    while(b != 0):
        temp = a % b
        a = b
        b = temp
    return a

t = int(input())

while(t > 0):
    t -= 1
    a = int(input())
    b = int(input())
    
    print(gcd(a, b))