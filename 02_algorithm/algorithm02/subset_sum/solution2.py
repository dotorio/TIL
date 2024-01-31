import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# 테스트 개수
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# 부분집합을 만들 전체 집합을 만든다.
for case in range(1, T + 1):
    N, K = map(int, input().split())
    # 테스트마다 부분집합의 길이와 부분집합의 합을 받는다.
    subset_cnt = 0
    # 조건에 맞는 부분집합의 개수를 0으로 지정한다.
    L = len(A)
    # 전체 집합의 길이를 L로 지정
    for i in range(1 << L):
        # 전체 집합의 부분집합 개수만큼 for문 실행
        subset = []
        # 부분집합으로 쓸 리스트 생성
        for j in range(L):
            # 전제 집합의 원소 수만큼 비트를 비교한다
            if i & (1 << j):
                # i의 j번 비트가 1인 경우
                subset.append(A[j])
                # 해당 원소를 부분집합에 넣는다.
        if len(subset) == N and sum(subset) == K:
            # 만들어진 부분집합의 길이와 합이 조건에 맞는다면
            subset_cnt += 1
            # 조건에 맞는 부분집합의 개수를 1 더한다.
    print(f'#{case} {subset_cnt}')
    # 케이스마다 최종 값을 출력한다.


