a = set()

f = open('CONTACT.in', 'r')

for line in f:
    a.add(line.strip().lower())
    
a = sorted(a)
for i in a:
    print(i)