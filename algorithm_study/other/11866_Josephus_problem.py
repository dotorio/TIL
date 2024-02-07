A, B = map(int, input().split())
arr = list(range(1, A+1))
new = []
i = 0
for _ in range(A):
    i += B-1
    len_arr = len(arr)
    while i >= len_arr:
        i -= len_arr
    new.append(arr.pop(i))

print(f'<{", ".join(map(str, new))}>')