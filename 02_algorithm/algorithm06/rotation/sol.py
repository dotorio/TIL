import sys
sys.stdin = open('input.txt')
from collections import deque

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     nums = deque(map(int, input().split()))
#     # 작업 수를 수열의 길이로 나눈 나머지만큼 회전시킨다
#     for _ in range(M % N):
#         nums.append(nums.popleft())
#     # 작업을 끝내고 맨 앞의 숫자를 출력한다
#     print(f'#{tc} {nums[0]}')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    # 작업 수를 수열의 길이로 나눈 나머지를 인덱스로 수열에서 출력한다
    print(f'#{tc} {nums[M % N]}')