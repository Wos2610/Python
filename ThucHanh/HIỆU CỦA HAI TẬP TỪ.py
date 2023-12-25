a = []
b = []
with open("DATA1.in") as input:
    while True:
        x = input.readline().lower()
        if x == "": break
        a.extend(x.split())
    c = set(a)
    
with open("DATA2.in") as input:
    while True:
        x = input.readline().lower()
        if x == "": break
        b.extend(x.split())
    d = set(b)

res1 = sorted(c - d)
res2 = sorted(d - c)
for i in res1:
    print(i, end = " ")
print()

for i in res2:
    print(i, end = " ")
print()