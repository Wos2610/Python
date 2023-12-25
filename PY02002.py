f = [0] * 106
def fibo():
    f[1] = 1
    f[2] = 1
    for i in range(3, 106):
        f[i] = f[i - 1] + f[i - 2]
        
t = int(input())
fibo()
while t > 0:
    t -= 1
    a, b = input().split()
    a = int(a)
    b = int(b)
    
    for i in range(a, b + 1):
        print(f[i], end = ' ')
    print()
    