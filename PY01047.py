m = [0] * 10000

def sieve():
    m[0] = m[1] = 1
    for i in range(2, 10000):
        if m[i] == 0:
            for j in range(i * i, 10000, i):
                m[j] = i
                
t = int(input())
sieve()
while(t > 0):
    t -= 1
    s = input()
    n = len(s)
    
    temp = s[-4:]
    if m[int(temp)] == 0: print("YES")
    else: print("NO")
        
                
