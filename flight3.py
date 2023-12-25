import json
a = []
with open('flights.json', 'r') as f:
    file = json.load(f)
    a = file['flights']

t = int(input())
for i in range(t):
    x, y = list(map(int, input().split()))
    sum = 0
    for j in a:
        if int(j['year']) >= x and int(j['year'])  <= y:
            sum += int(j['passengers'])
    if sum == 0: print("Invalid")
    else: print(sum)
       
    