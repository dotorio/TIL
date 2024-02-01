import sys
sys.stdin = open('input.txt')

for a in range(1, 11):
    # 총 10개의 테스트 케이스
    case = int(input())
    # 케이스 번호
    arr = []
    # 배열을 담을 리스트
    for j in range(100):
        arr.append(list(map(int, input().split())))
    # 100 * 100 배열을 input값을 받아 만든다. 
    max_sum = 0
    # 최댓값을 0으로 설정해둔다.
    diagonal_sum = 0
    diagonal_sum2 = 0
    # 두 대각선의 합을 0으로 설정해둔다.
    for x in range(100):
        if max_sum < sum(arr[x]):
            max_sum = sum(arr[x])
        # 각 행의 합 중에 최댓값을 max_sum에 할당
        row_sum = 0
        for y in range(100):
            row_sum += arr[y][x]
        if max_sum < row_sum:
            max_sum = row_sum
    # 각 열의 합 중에 최댓값이 새롭게 나온다면
    # max_sum에 할당
        diagonal_sum += arr[x][x]
        diagonal_sum2 += arr[x][99 - x]        
    if max_sum < diagonal_sum:
        max_sum = diagonal_sum
    if max_sum < diagonal_sum2:
        max_sum = diagonal_sum2
    # 두 대각선의 합을 구해 최댓값이 새롭게 나온다면
    # max_sum에 할당
    print(f'#{case} {max_sum}')
    # 최댓값을 출력한다.