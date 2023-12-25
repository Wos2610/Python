s = input()
while len(s) % 3 != 0 : s = "0" + s

res = ""
x = [4, 2, 1]
while len(s) != 0:
    tmp = s[:3]
    y = int(tmp[0]) * x[0] + int(tmp[1]) * x[1] + int(tmp[2]) * x[2]
    res += str(y)
    s = s[3:]
print(res)