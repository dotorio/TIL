T = int(input())
num = 0
for case in range(T):
    word = input()
    a = {}
    for i in word:
        if i not in a:
            a[i] = 1
    print(a)