t = int(input())

for i in range(t):
    s = input().split(" ")
    ans = s[0]
    for i in range(1, len(s)):
        if len(ans) + len(s[i]) + 1 > 100:
            break
        ans += " " + s[i]
    print(ans)