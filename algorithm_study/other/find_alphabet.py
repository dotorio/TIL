from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)
arr = [-1] * len(alphabet_list)
A = input()
for i in A:
    for j in alphabet_list:
        if i == j:
            arr[alphabet_list.index(j)] = A.index(i)
            break
print(" ".join(map(str, arr)))