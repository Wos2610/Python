n = int(input())

a = [int(x) for x in input().split()]
m = [0] * 30006
for i in a:
    m[i] += 1

for i in range(1, 3000006):
    if m[i] == 0:
        print(i)
        break
