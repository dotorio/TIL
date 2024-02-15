import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for _ in range(T):
    cmd = input()
    n = int(input())
    nums = input()
    cut = deque(nums[1:len(nums)-1].split(','))
    if cut[0] == "":
        cut = deque()
    i = 0
    rev = False
    result = True
    while i < len(cmd):
        if i < len(cmd)-1 and cmd[i:i+2] == 'RR':
            i += 2
        elif cmd[i] == 'R':
            i += 1
            if rev == False:
                rev = True
            else:
                rev = False
        else:
            if len(cut) == 0:
                result = False
                print('error')
                break
            i += 1
            if rev == True:
                cut.pop()
            else:
                cut.popleft()
    if rev == True:
        cut.reverse()
    if result == True:
        print(f'[{",".join(list(cut))}]')
# a= deque([1,2,3])
# print(f'[{",".join(list(a))}]')

# nums = input()
# cut = deque(nums[1:len(nums)-1].split(','))
# print(cut)
