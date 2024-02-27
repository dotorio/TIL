path = []
used = [False, False, False, False, False, False]

def KFC(x):
    if x == 2:
        print(*path)
        return
    for i in range(1,7):
        if used[i-1] == True : continue
        used[i-1] = True
        path.append(i)
        KFC(x+1)
        path.pop()
        used[i-1] = False
KFC(0)

path = []
used = [False, False, False, False, False, False]

def KFC(x):
    if x == 2:
        print(*path)
        return
    for i in range(1,7):
        path.append(i)
        KFC(x+1)
        path.pop()
KFC(0)