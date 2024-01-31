import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# 테스트 개수
for a in range(1, T + 1):
    # 각 테스트마다
    N = int(input())
    # 색칠하는 영역의 수를 받는다
    arr = [[0] * 10 for _ in range(10)]
    # 색칠할 영역 10 * 10의 배열을 만든다
    for b in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[j][i] += 1
    # 색칠하는 영역에 해당하는 값을 1 더한다.
    result = 0
    for b in arr:
        result += b.count(2)
    # 빨강과 파랑을 둘다 칠했다면 그 영역의 값이 2이므로 2의 개수를 탐색해서 출력한다.
    # 같은 색은 영역이 겹치지 않기 때문에 문제없이 출력된다.
    print(f'#{a} {result}')