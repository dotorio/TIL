import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# 테스트 개수
A = list(range(1, 13))
# 부분집합을 만들 전체 집합을 만든다.
subsets = [[]]
# 부분집합을 넣을 리스트를 만든다. 공집합은 미리 넣어둔다.
for a in A:
    L = len(subsets)
    for i in range(L):
        subsets.append(subsets[i] + [a])
# 부분집합 전부를 리스트에 넣는다.
for case in range(1, T + 1):
    N, K = map(int, input().split())
    # 테스트마다 부분집합의 길이와 부분집합의 합을 받는다.
    subset_cnt = 0
    # 조건에 맞는 부분집합의 개수를 0으로 지정한다.
    for subset in subsets:
        if len(subset) == N and sum(subset) == K:
            subset_cnt += 1
    # 부분집합마다 길이와 합이 조건에 맞다면 해당 개수를 1 더한다.
    print(f'#{case} {subset_cnt}')
    # 완성된 값을 출력한다.




