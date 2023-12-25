import cmath
t = int(input())

while t > 0:
    t -= 1
    arr = [int(x) for x in input().split()]
    
    a = complex(arr[0], arr[1])
    b = complex(arr[2], arr[3])
    
    c = (a + b) * a
    d = (a + b) ** 2 
    print("{:.0f} + {:.0f}i, {:.0f} + {:.0f}i".format(c.real, c.imag, d.real, d.imag))
    