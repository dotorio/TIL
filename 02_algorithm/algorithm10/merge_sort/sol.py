import sys
sys.stdin = open('input.txt')
from collections import deque

def merge_sort(num):
    # 쪼갠 배열의 길이가 1이라면 그대로 리턴
    if len(num) == 1:
        return num
    # 배열의 길이가 2 이상이라면 쪼갠다
    left, right = merge_sort(num[:len(num)//2]), merge_sort(num[len(num)//2:])
    # 쪼갠 배열을 병합한다
    return merge(left, right)

def merge(left, right):
    global cnt
    left, right = deque(left), deque(right)
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) or len(right):
        if len(left) and len(right):
            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
        elif len(left):
            result.append(left.popleft())
        elif len(right):
            result.append(right.popleft())
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    num = list(map(int, input().split()))
    answer = merge_sort(num)
    print(f'#{tc} {answer[N//2]} {cnt}')