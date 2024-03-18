import sys
sys.stdin = open('input.txt')
from collections import deque

def merge_sort(num):
    if len(num) == 1:
        return deque(num)
    left, right = num[:len(num)//2], num[len(num)//2:]
    merge_sort(left)
    merge_sort(right)
    return merge(deque(left), deque(right))

def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    while left and right:  # 두 데크 모두 비어있지 않은 경우에만 반복
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    while left:  # 왼쪽 데크가 비어있지 않은 경우 남은 요소를 추가
        result.append(left.popleft())
    while right:  # 오른쪽 데크가 비어있지 않은 경우 남은 요소를 추가
        result.append(right.popleft())
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    cnt, result = 0. []
    num = list(map(int, input().split()))
    merge_sort(num)
    print(f'#{tc} {result[N//2]} {cnt}')
