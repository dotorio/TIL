import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
wiki1 = {}
wiki2 = {}
for i in range(1, N+1):
    name = input()
    wiki1[i] = name
    wiki2[name] = i
for i in range(M):
    Q = input()
    if Q.isdigit():
        print(wiki1[int(Q)])
    else:
        print(wiki2[Q])
