import sys
sys.stdin = open('input.txt')
import copy

for tc in range(1, int(input())+1):
    num, change = input().split()
    ch = int(change)
    num_list = list(num)
    while ch:
        max_num = max(num_list)
        max_cnt = num_list.count(max_num)
        for i in num_list:
            if i 
        for i in range(len(num_list)):
            if num_list[i] != if_max[i]:
                rev_num = num_list[::-1]
                num_list[i], num_list[len(num_list)-1-rev_num.index(if_max[i])] = num_list[len(num_list)-1-rev_num.index(if_max[i])], num_list[i]
                ch -= 1
    print(f'#{tc} {"".join(map(str, num_list))}')
