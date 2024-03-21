import sys
sys.stdin = open('input.txt')

def f(past, now):
    # 전의 높이와 지금 높이를 비교
    # 전의 높이가 더 크거나 같으면
    if past >= now:
        # 1 반환
        return 1
    # 지금 높이가 더 크면
    else:
        # 1 + 그 차이만큼 반환
        return 1 + now - past

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # sum_arr = 칸마다 최소 연료 소비량을 저장함
    sum_arr = [[0] * N for _ in range(N)]
    # 행렬을 순회하며 sum_arr를 완성
    for i in range(N):
        for j in range(N):
            # from_up : 위쪽에서 올 때의 연료 소비량
            # from_left : 왼쪽에서 올 때의 연료 소비량
            from_up, from_left = 0, 0
            if 0 <= i-1:
                from_up = sum_arr[i-1][j] + f(arr[i-1][j], arr[i][j])
            if 0 <= j-1:
                from_left = sum_arr[i][j-1] + f(arr[i][j-1], arr[i][j])
            # 만약 둘 다 0이 아니라면
            if from_up and from_left:
                # 둘 중 작은 값을 할당
                sum_arr[i][j] = min(from_left, from_up)
            # 만약 둘 중 하나라도 0이면
            else:
                # 둘 중 큰 값을 할당
                sum_arr[i][j] = max(from_left, from_up)
    # sum_arr의 마지막 값을 출력
    print(f'#{tc} {sum_arr[N-1][N-1]}')