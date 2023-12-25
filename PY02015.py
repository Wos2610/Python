while True:
    arr = list(map(int, input().split(" ")))

    if arr[0] == 0 and arr.count(arr[0]) == len(arr) : break
    d = 0
    while(arr.count(arr[0]) != len(arr)):
        d += 1
        x = arr[0]
        for i in range(0, 3):
            arr[i] = abs(arr[i] - arr[i + 1])
        arr[3] = abs(arr[3] - x)
    print(d)
        