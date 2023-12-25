def check(s):
    sum = 0
    for i in s:
        sum += int(i)
        
    sum = str(sum)
    if len(sum) > 1 and sum == sum[::-1]: return True
    return False

t = int(input())

while(t > 0):
    t -= 1
    n = input()
    if check(n) == True: print("YES")
    else: print("NO")
    
    