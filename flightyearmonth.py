import json
a = []
with open('flights.json', 'r') as f:
    file = json.load(f)
    a = file['flights']
    
t = int(input())
for i in range(t):
    x, y = input().split()
    sum = 0
    for j in a:
        if j['year'] == x and j['month'] == y:
            sum += int(j['passengers'])
        
    if sum == 0: print("Invalid")
    else: print(sum)