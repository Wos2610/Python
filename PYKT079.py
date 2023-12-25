t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l = min(a)
    r = max(a)
    
    b = set(a)
    print(r - l + 1 - len(b))