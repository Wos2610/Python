while True:
    n = int(input())
    if n == 0: break
    
    save = []
    save.append(n)
    while n != 1:
        if n % 2 == 0: n //= 2
        else: n = 3*n + 1
        save.append(n)
    
    print(len(save))
        