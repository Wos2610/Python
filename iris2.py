import csv

a = []
with open('iris.csv', 'r') as f:
    file = csv.reader(f)
    for i in file:
        a.append(i)
        
def arg(b):
    res = 0
    for i in b:
        res += i
    return res/len(b)

def sum(b):
    res = 0
    for i in b:
        res += i
    return res

t = int(input())
for i in range(t):
    x, y, z = input().split()
    t = 0
    if y == "sepal_length": t = 0
    elif y == "sepal_width": t = 1
    elif y == "petal_length": t = 2
    elif y == "petal_width": t = 3
    else: print("Invalid")
    
    ok = 0
    h = []
    for j in a:
        if j[4] == x:
            ok = 1
            h.append(float(j[t]))
    if ok == 0: print("Invalid")
    else:
        if z == "min":
            print(min(h))
        elif z == "max":
            print(max(h))
        elif z == "sum":
            print(sum(h))  
        elif z == "arg":
            print(arg(h))
    