small = []
for _ in range(9):
    S = int(input())
    small.append(S)
small.sort()
for i in small:
    small.remove(i)
    for j in small:
        small.remove(j)
        if sum(small) == 100:
            for _ in range(7):
                print(small[_])
            quit()
        small.append(j)
        small.sort()
    small.append(i)
    small.sort()