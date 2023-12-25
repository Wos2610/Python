class Number:
    def __init__(self, num) :
        self.num = num
        self.sum = 0
        for i in num:
            self.sum += int(i)
            
    def __lt__(self, other):
        if self.sum == other.sum:
            return int(self.num) < int(other.num)
        return self.sum < other.sum
    
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    
    a = input().split()
    l = []
    for i in a:
        l.append(Number(i))
    l.sort()
    
    for i in l:
        print(i.num, end=' ')
    print()