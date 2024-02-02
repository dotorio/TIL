A, B = map(int, input().split())
C = int(input())

D = C // 60
E = C % 60
A += D
B += E
if B > 59:
    B -= 60
    A += 1
if A > 23:
    A -= 24
arr = [A, B]
print(" ".join(map(str, arr)))