A, B = map(int, input().split())
B -= 45
if B < 0:
    A -= 1
    B += 60
if A < 0:
    A += 24
arr = [A, B]
print(" ".join(map(str, arr)))