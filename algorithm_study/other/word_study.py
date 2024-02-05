A = str(input()).upper()
B = {}
C = []
max_alpha = 0
for i in range(len(A)):
    B[A[i]] = 0
for i in range(len(A)):
    B[A[i]] += 1
for i in B:
    if max_alpha < B[i]:
        max_alpha = B[i]
for i in B:
    if max_alpha == B[i]:
        C.append(i)
if len(C) > 1:
    print('?')
else:
    print(C[0])