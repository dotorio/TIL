import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    V, E = map(int, input().split())
    worktree = [[] for _ in range(V+1)]
    work = list(map(int, input().split()))
    seq = []
    for k in range(E):
        worktree[work[2*k+1]].append(work[2*k])
    result = False
    while result == False:
        cnt = 0
        for i in range(1, V+1):
            if not worktree[i]:
                if i not in seq:
                    seq.append(i)
                for j in range(1, V+1):
                    if i in worktree[j]:
                        worktree[j].remove(i)
            else:
                cnt += 1
        if cnt == 0:
            result = True
    print(f'#{tc} {" ".join(map(str, seq))}')



