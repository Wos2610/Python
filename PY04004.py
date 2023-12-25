def gcd(a, b):
        while b != 0:
            tmp = a % b
            a = b
            b = tmp
        return a
    
class PS:
    def rutgon(self):   
        k = gcd(self.tu, self.mau)
        self.tu = self.tu/k
        self.mau = self.mau/k
        return self
        
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def sum(self, other):
        res = PS(0, 1) 
        res.mau = self.mau * other.mau
        res.tu = self.tu * other.mau + self.mau * other.tu
        
        return res
      
    def __str__(self) :
        return "{:.0f}/{:.0f}".format(self.tu, self.mau)
    
    
a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
p = PS(a, b).rutgon()
q = PS(c, d).rutgon()
print(p.sum(q).rutgon())
