T = int(input())

dic = {1:1, 2:2, 3:4}
def plus(A):
    if A in dic:
        return dic[A]
    dic[A] = plus(A-3) + plus(A-2) + plus(A-1)
    return dic[A]
for _ in range(T):
    print(plus(int(input())))