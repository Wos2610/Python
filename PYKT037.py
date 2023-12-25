x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
     'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
     'W', 'X', 'Y', 'Z']
def change(a, b):
    res = ""
    while True:
        res += str(x[a % b])
        a //= b
        if a == 0: break
    print(res[::-1])
    
n = int(input())
while n > 0:
    n -= 1
    arr = input().split()
    if len(arr) == 1 : arr.append(input())
    a = int(arr[0])
    b = int(arr[1])
    change(a, b)
        