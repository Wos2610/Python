def is_unique_sequence(a):
    def is_unique(subsequence):
        return any(subsequence.count(x) == 1 for x in subsequence)

    for start in range(len(a)):
        for end in range(start + 1, len(a) + 1):
            if not is_unique(a[start:end]):
                return False
    return True

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    sequence = [int(x) for x in input().split()]
    print('YES' if is_unique_sequence(sequence) else 'NO')