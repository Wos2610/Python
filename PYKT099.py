with open ('DATA1.in') as f:
    set1 = set(f.read().lower().split())

with open('DATA2.in') as f:
    set2 = set(f.read().lower().split())
a = []
b = []
for i in set1:
    if i not in set2:
        a.append(i)

for i in set2:
    if i not in set1:
        b.append(i)
        
a.sort()
b.sort()
for i in a:
    print(i, end = " ")
print()
for i in b:
    print(i, end = " ") 
    