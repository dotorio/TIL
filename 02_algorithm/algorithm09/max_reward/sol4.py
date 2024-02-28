import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    num, ch = input().split()
    change_cnt = int(ch)
    num_list = list(num)
    len_num = len(num_list)
    if_max = num_list[:]
    if_max.sort(reverse=True)
    for _ in range(change_cnt):
        if num_list == if_max:
            num_list[-2], num_list[-1] = num_list[-1], num_list[-2]
        else:
            change_list = []            
            for i in range(len_num):
                for j in range(len_num):
                    if i == j:
                        continue
                    else:
                        new = num_list[:]
                        new[i], new[j] = new[j], new[i]
                        change_list.append(new)
            num_list = max(change_list)
    print(f'#{tc} {"".join(num_list)}')