n = int(input())
a = {}
d = 0
str = ""
for i in range(n):
    line = input()
    if line == "":
        d = 0
        str = ""
        continue
    
    if d == 0:
        d = 1
        str = line
        a[str] = 0
    else:
        a[str] += 1

for i in a:
    print("{}: {}".format(i, a[i]))
        
    