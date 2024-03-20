import sys
sys.stdin = open('input.txt')

def f(stack):
    last_max_num = 0
    new_s = []
    while stack:
        now = stack.pop()
        if not visit[now]:
            visit[now] = True
            last_max_num = max(last_max_num, now)
            for next in cal[now]:
                if not visit[next]:
                    new_s.append(next)
    if new_s:
        return f(new_s)
    return last_max_num

for tc in range(1, 11):
    d_len, start = map(int, input().split())
    data = list(map(int, input().split()))
    cal = {i:[] for i in range(1, 101)}
    visit = [False]*101
    for i in range(len(data)//2):
        cal[data[2*i]].append(data[2*i+1])
    stack = [start]
    print(f'#{tc} {f(stack)}')