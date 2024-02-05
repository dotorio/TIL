import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for i in range(N)]
    for i in arr:
        for j in range(N-M+1):
            word = i[j:j+M]
            if "".join(map(str,word)) == "".join(map(str,word[::-1])):
                print(f'#{case} {"".join(map(str,word))}')
    arr = zip(*arr[::-1])
    for i in arr:
        for j in range(N-M+1):
            word = i[j:j+M]
            if "".join(map(str,word)) == "".join(map(str,word[::-1])):
                print(f'#{case} {"".join(map(str,word))}')
                