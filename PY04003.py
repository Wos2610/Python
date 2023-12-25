def gcd(a, b):
        while b != 0:
            tmp = a % b
            a = b
            b = tmp
        return a
    
class PS:
    def __init__(self, tu, mau):
        k = gcd(tu, mau)
        self.tu = tu/k
        self.mau = mau/k
        
    def __str__(self) :
        return "{:.0f}/{:.0f}".format(self.tu, self.mau)
    
    
a, b = input().split()
a = int(a)
b = int(b)
p = PS(a, b)
print(p)
