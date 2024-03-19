import sys
sys.stdin = open('input.txt')

# 4방향을 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def f(cnt, i, j, now_str):
    # 만약 7자리가 완성되었다면
    if cnt == 7:
        # 세트에 넣고 리턴
        num.add(now_str)
        return
    # 4방향으로 갈 수 있는 곳이면
    for k in range(4):
        if 0<=i+dx[k]<4 and 0<=j+dy[k]<4:
            # 문자열에 추가해가면서 함수 호출
            f(cnt+1, i+dx[k], j+dy[k], now_str+str(arr[i+dx[k]][j+dy[k]]))

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 중복 제거를 위해 세트로 만든다
    num = set()
    # 각 좌표마다 함수 출력
    for i in range(4):
        for j in range(4):
            f(1, i, j, str(arr[i][j]))
    # 완성된 num의 원소 개수를 출력
    print(f'#{tc} {len(num)}')