N = int(input())
cards = list(range(1, N+1))


def discard(C):
    if len(C) == 1:
        return C[0]
    if len(C) % 2 == 1:
        A = C[1::2]
        A.append(A.pop(0))
    else:
        A = C[1::2]
    return discard(A)

print(discard(cards))