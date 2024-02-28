import sys
sys.stdin = open('input.txt')

def change(a):
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
    return max(change_list)

def final_change(a, b):
    global final
    len_num = len(a)
    for i in range(len_num):
        for j in range(len_num):
            if i == j:
                continue
            else:
                new = a[:]
                new[i], new[j] = new[j], new[i]
                if b == 2:
                    new_2 = new[:]
                    final_change(new_2, b-1)
                if b == 1:
                    final.append(new)


for tc in range(1, int(input())+1):
    num, ch = input().split()
    change_cnt = int(ch)
    num_list = list(num)
    if change_cnt >= 3:
        for _ in range(change_cnt-2):
            change(num_list)
        change_cnt = 2
    if change_cnt == 2:
        final = []
        final_change(num_list, 2)
        print(f'#{tc} {"".join(max(final))}')
    if change_cnt == 1:
        change(num_list)
        print(f'#{tc} {"".join(change(num_list))}')