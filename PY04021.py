from datetime import datetime
import re

class Gamer:
    def __init__(self, ma, name, start, end):
        self.ma = ma
        self.name = re.sub(' +', ' ', name)
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M")
        self.seconds = (end_time - start_time).total_seconds()
        self.hours = self.seconds // 3600
        self.minutes = (self.seconds - self.hours * 3600) / 60
    
    def __lt__(self, other):
        return self.seconds > other.seconds
    
    def __str__(self) -> str:
        return "{:s} {:s} {:.0f} gio {:.0f} phut\n".format(self.ma, self.name, self.hours, self.minutes)
        
n = int(input())
save = []
while n > 0:
    n -= 1
    save.append(Gamer(input(), input(), input(), input()))
save.sort()
for i in save:
    print(i)
    
    