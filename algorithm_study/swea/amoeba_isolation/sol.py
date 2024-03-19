import sys
sys.stdin = open('input.txt')

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]
change = [0, 2, 1, 4, 3]

def f(loc, num_list, dir_list):
    for _ in range(M):
        new_loc, new_num, new_dir, several = [], [], [], []
        for k in range(len(loc)):
            new_i, new_j = loc[k][0] + dy[dir_list[k]], loc[k][1] + dx[dir_list[k]]
            several.append([[num_list[k], dir_list[k]]])
            for idx, value in enumerate(new_loc):
                if value == [new_i, new_j]:
                    several[idx].append([num_list[k], dir_list[k]])
                    new_num[idx] += num_list[k]
                    new_dir[idx] = max(several[idx])[1]
                    break
            else:                
                if new_i in [0, N-1] or new_j in [0, N-1]:
                    if num_list[k]//2:
                        new_loc.append([new_i, new_j])
                        new_num.append(num_list[k]//2)
                        new_dir.append(change[dir_list[k]])
                else:
                    new_loc.append([new_i, new_j])
                    new_num.append(num_list[k])
                    new_dir.append(dir_list[k])
        loc, num_list, dir_list = new_loc, new_num, new_dir

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    loc, num_list, dir_list = [], [], []
    for _ in range(K):
        i, j, num, dir = map(int, input().split())
        loc.append([i, j])
        num_list.append(num)
        dir_list.append(dir)
    f(loc, num_list, dir_list)
    print(f'#{tc} {sum(num_list)}')