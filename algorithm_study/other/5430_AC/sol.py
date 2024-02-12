import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    nums = input()
    if nums == '[]':
        arr = deque()
    else:
        arr = deque(map(int, nums[1:-1].split(',')))
    result = True
    i = 0
    while i < len(p):
        if p[i] == 'R':
            if i+1 < len(p) and p[i+1] == 'R':
                i += 2
            else:
                arr.reverse()
                i += 1
        elif p[i] == 'D':
            if len(arr) == 0:
                print('error')
                result = False
                break
            else:
                arr.popleft()
                i += 1
    if result == True:
        print('[', end = '')
        for i in arr:
            if i == arr[-1]:
                print(f'{i}]')
            else:
                print(str(i)+',', end = '')


