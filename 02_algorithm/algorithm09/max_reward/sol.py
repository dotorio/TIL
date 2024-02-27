import sys
sys.stdin = open('input.txt')
import copy

for tc in range(1, int(input())+1):
    num, change = input().split()
    ch = int(change)
    num_list = list(num)
    if_max = copy.deepcopy(num_list)
    if_max.sort(reverse = True)
    if len(num_list)-1 <= ch:
        print(f'#{tc} {"".join(map(str, if_max))}')
    else:
        for i in range(len(num_list)):
            if ch == 0:
                break
            if num_list[i] != if_max[i]:
                rev_num = num_list[::-1]
                num_list[i], num_list[len(num_list)-1-rev_num.index(if_max[i])] = num_list[len(num_list)-1-rev_num.index(if_max[i])], num_list[i]
                ch -= 1
        print(f'#{tc} {"".join(map(str, num_list))}')