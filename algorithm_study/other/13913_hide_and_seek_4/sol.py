from collections import deque

def f(num, cnt, stack):
    global min_cnt
    if num == K:
        if min_cnt > cnt:
            min_cnt = cnt
            answer = stack
            return answer
    elif num > K:
        if min_cnt > cnt + num - K:
            min_cnt = cnt + num - K
            answer = stack + list(range(num-1, K-1, -1))
            return answer
    else:
        f(num*2, cnt+1, stack + [num*2])
        f(num+1, cnt+1, stack + [num+1])
        f(num-1, cnt+1, stack + [num-1])

        

N, K = map(int, input().split())
min_cnt = 100000
queue = deque()
queue.append(())

print(min_cnt)
print(answer)
