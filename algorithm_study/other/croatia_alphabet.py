A = list(map(str, input()))
alphabet = 0
while A != []:
    if A[0] == 'c':
        if 2 <= len(A) and A[1] == '=':
            alphabet += 1
            A.pop(0)
            A.pop(0)
        elif 2 <= len(A) and A[1] == '-':
            alphabet += 1
            A.pop(0)
            A.pop(0)
        else:
            alphabet += 1
            A.pop(0)
    if A == []:break
    if A[0] == 'd':
        if 2 <= len(A) and A[1] == '-':
            alphabet += 1
            A.pop(0)
            A.pop(0)
        elif 3 <= len(A) and A[1] == 'z' and A[2] == '=':
            alphabet += 1
            A.pop(0)
            A.pop(0)
            A.pop(0)
        else:
            alphabet += 1
            A.pop(0)
    if A == []:break
    if A[0] == 'l':
        if 2 <= len(A) and A[1] == 'j':
            alphabet += 1
            A.pop(0)
            A.pop(0)
        else:
            alphabet += 1
            A.pop(0)
    if A == []:break
    if A[0] == 'n':
        if 2 <= len(A) and A[1] == 'j':
            alphabet += 1
            A.pop(0)
            A.pop(0)
        else:
            alphabet += 1
            A.pop(0)
    if A == []:break
    if A[0] == 's':
        if 2 <= len(A) and A[1] == '=':
            alphabet += 1
            A.pop(0)
            A.pop(0)
        else:
            alphabet += 1
            A.pop(0)
    if A == []:break
    if A[0] == 'z':
        if 2 <= len(A) and A[1] == '=':
            alphabet += 1
            A.pop(0)
            A.pop(0)
        else:
            alphabet += 1
            A.pop(0)
    if A == []:break
    if A[0] not in ['c', 'd', 'l', 'n', 's', 'z']:
        alphabet += 1
        A.pop(0)

print(alphabet)