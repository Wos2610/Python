n = input()
d = 0
for i in n:
    if i == '4' or i == '7' : d += 1
if d == 4 or d == 7:
    print("YES")
else:
    print("NO")