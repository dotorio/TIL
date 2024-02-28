import sys
sys.stdin = open('input.txt')

def change(a, b):
    for _ in range(b):
        if a == if_max:
            a[-2], a[-1] = a[-1], a[-2]
        else:
            change_list = []
            len_num = len(a)
            for i in range(len_num):
                for j in range(len_num):
                    if i == j:
                        continue
                    else:
                        new = a[:]
                        new[i], new[j] = new[j], new[i]
                        change_list.append(new)
            a = max(change_list)

for tc in range(1, int(input())+1):
    num, ch = input().split()
    change_cnt = int(ch)
    num_list = list(num)
    if_max = num_list[:]
    if_max = if_max.sort(reverse=True)
    change(num_list, change_cnt)
    print(f'#{tc} {"".join(num_list)}')