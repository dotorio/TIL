from collections import deque

N, M = map(int, input().split())

def f(num, cnt, arr):
    if num == N+1 or cnt == M:
        return
    f(num+1, cnt, arr)
    arr.append(num)
    cnt += 1
    if cnt == M:
        print(arr[::-1])
        return
    return f(num+1, cnt, arr)

f(1, 0, [])