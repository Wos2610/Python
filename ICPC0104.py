t = int(input())
while t > 0:
    t -= 1
    s = input()
    n = len(s)
    
    tmp = 0
    arr = []
    for i in s:
        if i.isdigit(): tmp = tmp * 10 + int(i)
        else: 
            if tmp != 0: 
                arr.append(tmp)
                tmp = 0
    if tmp != 0: arr.append(tmp)
    
    res = 10**18
    
    for i in arr:
        res = min(res, i)
    print(res)
    