def process(s):
    n = len(s)
    tich = 1
    mark = 0
    for i in range(0, n, 2):
        if s[i] != '0': 
            tich *= int(s[i])
            mark = 1    
    sum = 0  
    for i in range(1, n, 2):
        sum += int(s[i])  
    if mark == 0: tich = 0
    print(f"{tich} {sum}\n")

t = int(input())
while(t > 0):
    t -= 1
    s = input()
    process(s)