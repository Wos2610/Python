class Student:
    def __init__(self, name, correct, submit):
        self.name = name
        self.correct = correct
        self.submit = submit
    
    def __lt__(self, other):
        if self.correct == other.correct:
            if self.submit == other.submit:
                return self.name < other.name
            return self.submit < other.submit
        return self.correct > other.correct
        

n = int(input())
a = []
for i in range(n):
    s = input()
    c, d = input().split()
    c = int(c)
    d = int(d)
    a.append(Student(s, c, d))
    
a.sort()

for i in a:
    print(i.name, i.correct, i.submit)