class Ten:
    ho = ""
    ten = ""
    dem = ""
    def __init__(self, name):
        self.name = chuanHoa(name)
        b = self.name.split()
        self.ten = b[len(b) - 1]
        self.ho = b[0]
        for i in range(1, len(b) - 1):
            self.dem += b[i]
            if i != len(b) - 2:
                self.dem += " "
    
    def __lt__(self, other):
        if self.ten == other.ten:
            if self.ho == other.ho:
                return self.dem < other.dem
            return self.ho < other.ho
        return self.ten < other.ten
    
    def __str__(self):
        return self.name
            
def chuanHoa(s):
    a = s.strip().split()
    res = ""
    for i in range(len(a)):
        res += a[i][:1].upper() + a[i][1:].lower()
        if i != len(a) - 1:
            res += " "
    return res

a = []
with open ('DANHSACH.in', 'r') as f:
    while True:
        tmp = f.readline()
        if tmp == "":
            break
        a.append(Ten(tmp))

a.sort()
for i in a:
    print(i)