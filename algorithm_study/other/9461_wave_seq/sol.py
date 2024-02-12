import sys
input = sys.stdin.readline

def seq(A):
    if A in length:
        return length[A]
    else:
        length[A] = seq(A-3) + seq(A-2)
        return length[A]
        


T = int(input())
length = {0:0, 1:1, 2:1}
for _ in range(T):
    print(seq(int(input())))