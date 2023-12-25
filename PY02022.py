m = [0] * 1000006
         
def sieve():
    m[0] = m[1] = 1
    for i in range(2, 1000006):
        if m[i] == 0:
            for j in range(i * i, 1000006, i):
                m[j] = i

n = int(input())
sieve()
a = [int(x) for x in input().split()]

d = [0] * 1000006
for i in a:
    if m[i] == 0: d[i] += 1
    
for i in a:
    if d[i] != 0: 
        print(i, d[i])
        d[i] = 0
    

        


