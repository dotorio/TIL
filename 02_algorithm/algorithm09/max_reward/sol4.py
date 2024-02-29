import sys
sys.stdin = open('input.txt')

def change(a, b):
    global change_dict
    if b == change_cnt:
        return
    for i in range(len_num-1):
        for j in range(i+1, len_num):
            a[i], a[j] = a[j], a[i]
            if a in change_dict[b+1]:
                a[i], a[j] = a[j], a[i]
                continue
            new = a[:]
            change_dict[b+1].append(new)
            change(new, b+1)
            a[i], a[j] = a[j], a[i]

for tc in range(1, int(input())+1):
    num, ch = input().split()
    change_cnt = int(ch)
    change_dict = {}
    for i in range(1, change_cnt+1):
        change_dict[i] = []
    num_list = list(num)
    len_num = len(num_list)
    change(num_list, 0)
    print(f'#{tc} {"".join(max(change_dict[change_cnt]))}')