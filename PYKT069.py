from datetime import datetime
class CaThi:
    ma = ""
    date = ""
    def __init__(self, id, day, time, room):
        self.id = id
        self.ma = "C{:03d}".format(id)
        self.day = day
        self.time = time
        self.date = datetime.strptime(day + " " + time, '%d/%m/%Y %H:%M')
        self.room = room
    
    def __lt__(self, other):
        return self.date < other.date  
    def __str__(self):
        return self.ma + " " + self.day + " " + self.time + " " + self.room

f = open('CATHI.in', 'r')
n = int(f.readline())
a = []
for i in range(n):
    a.append(CaThi(i+1, f.readline().strip(), f.readline().strip(), f.readline().strip()))
a.sort()
for i in a:
    print(i)