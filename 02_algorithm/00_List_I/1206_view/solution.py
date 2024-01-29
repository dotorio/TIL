import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input()) # 건물의 개수
    arr = list(map(int, input().split())) # 건물의 높이
    cnt_bui = 0 # 조망권 확보된 세대 수
    for j in range(2, N-2):
        new_list = [arr[j-2], arr[j-1], arr[j+1], arr[j+2]]
        if arr[j] > max(new_list):
            cnt_bui += arr[j] - max(new_list)
    print(f'#{i+1} {cnt_bui}')