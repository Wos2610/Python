m = [0] * 100
a = [0] * 100
def Try(i, n):
    if i == n + 1:
        for j in range(1, n + 1):
            print(s[a[j]], end="")
        print()
        return
    for j in range(n):
        if m[j] == 0:
            m[j] = 1
            a[i] = j
            Try(i + 1, n)
            m[j] = 0
s = input()
n = len(s)
Try(1, n)
