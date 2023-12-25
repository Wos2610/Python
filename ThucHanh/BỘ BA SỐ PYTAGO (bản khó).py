def count_pythagorean_triples(N):
    count = 0
    for a in range(1, N):
        for b in range(a, N):
            for c in range(1, N):
                if (a * a + b * b) % N == c * c % N:
                    count += 1
                    print(a, b, c)
    return count
n = int(input())
result = count_pythagorean_triples(n)
print(result)