import csv
a = []
with open('iris.csv', 'r') as f:
    file = csv.reader(f)
    for lines in file:
        a.append(lines)


t = int(input())
for i in range(t):
    l, p = input().split()

    sum = 0
    d = 0
    for i in a:
        if i[4] == l and i[2] == p:
            sum += float(i[0])
            d += 1

    if sum != 0: print(sum/d)
    else: print("Invalid")
        
        


    
