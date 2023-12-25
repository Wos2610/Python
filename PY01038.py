t = int(input())

for i in range(t):
    n = int(input())
    for j in range(1000):
        if(n % 7 == 0): 
            print(n)
            break
        n += int(str(n)[::-1])

    if n % 7 != 0: print(-1)
    