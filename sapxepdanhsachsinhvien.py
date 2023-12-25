class SinhVien:
    ten = ""
    ho = ""
    dem = ""
    
    def __init__(self, ma, name, phone, mail):
        self.ma = ma
        self.name = name
        a = name.split()
        self.ten = a[len(a) - 1]
        self.ho = a[0]
        for i in range(1, len(a) - 1):
            self.dem += a[i]
            if i != len(a) - 2: self.dem += ' '
        self.phone = phone
        self.mail = mail
    
    def __lt__(self, other):
        if self.ten == other.ten:
            if self.ho == other.ho:
                if self.dem == other.dem:
                    return self.ma < other.ma
                return self.dem < other.dem
            return self.ho < other.ho
        return self.ten < other.ten

    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.name, self.phone, self.mail)
    
n = int(input())
a = []
for i in range(n):
    a.append(SinhVien(input(), input(), input(), input()))
a.sort()
for i in a:
    print(i)