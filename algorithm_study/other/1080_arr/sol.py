import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
answer = [list(input()) for _ in range(N)]
# 행 수나 열 수가 3보다 작다면
# 바꿀 필요 없이 바로 비교해서 결과 낸다
if N < 3 or M < 3:
    if arr == answer:
        print(0)
    else:
        print(-1)
else:
    cnt = 0
    # 행 수-2, 열 수-2만큼 행렬 순회하면서
    # 값이 다르면 3*3만큼 바꾸고 cnt 1 올린다
    for i in range(N-2):
        for j in range(M-2):
            if arr[i][j] != answer[i][j]:
                cnt += 1
                for k1 in range(3):
                    for k2 in range(3):
                        if arr[i+k1][j+k2] == '1':
                            arr[i+k1][j+k2] = '0'
                        else:
                            arr[i+k1][j+k2] = '1'
    # 행렬이 정답과 같으면 cnt 출력
    # 다르면 -1 출력
    if arr == answer:
        print(cnt)
    else:
        print(-1)