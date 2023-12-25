def count_pythagorean_triples(N):
    mp = {}
    for i in range(N):
        if mp.get(i * i % N) == None:
            mp[i * i % N] = 1
        else:
            mp[i * i % N] += 1
    count = 0

    for a in range(1, N):
        for b in range(a, N):
            c_square_mod_N = (a * a + b * b) % N
            if c_square_mod_N in mp and c_square_mod_N != 0:
                count += mp[c_square_mod_N]
    return count

N = int(input())
result = count_pythagorean_triples(N)
print(result)