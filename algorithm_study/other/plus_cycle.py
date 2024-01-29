N = int(input())
def cycle(n, x):
    if n >= 10:
        new_n = ((n % 10) * 10) + (n // 10 + n % 10)
        if (n // 10 + n % 10) >= 10:
            new_n -= 10
    else:
        new_n = n*11
    x += 1
    if N == new_n:
        return x
    else:
        return cycle(new_n, x)
result = cycle(N, 0)
print(result)