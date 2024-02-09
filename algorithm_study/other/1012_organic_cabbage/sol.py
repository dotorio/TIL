import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    fields = list([0] * M for _ in range(N))
    fields2 = list([False] * M for _ in range(N))
    for _ in range(K):
        i, j = map(int, input().split())
        fields[j][i] = 1
    cnt = 0
    con = {}
    for j in range(N):
        for i in range(M):
            con[(j, i)] = []
    for j in range(N):
        for i in range(M):
            if fields[j][i] == 1:
                if i-1 >= 0 and fields[j][i-1] == 1:
                    con[(j, i)].append([j, i-1])
                if j-1 >= 0 and fields[j-1][i] == 1:
                    con[(j, i)].append([j-1, i])
                if i+1 <= M-1 and fields[j][i+1] == 1:
                    con[(j, i)].append([j, i+1])
                if j+1 <= N-1 and fields[j+1][i] == 1:
                    con[(j, i)].append([j+1, i])
    for j in range(N):
        for i in range(M):
            if fields[j][i] == 1 and fields2[j][i] == False:
                stack = []
                stack.extend(con[(j, i)])
                fields2[j][i] = True
                while stack:
                    now = stack.pop()
                    if fields2[now[0]][now[1]] == False:
                        fields2[now[0]][now[1]] = True
                        stack.extend(con[(now[0], now[1])])
                cnt += 1
    print(cnt)
