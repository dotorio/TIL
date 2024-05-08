from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# permutations으로 순열들의 리스트를 받아
# set으로 중복을 없애고
# sorted list로 정렬한 리스트로 만든다
answer = sorted(list(set(permutations(nums, M))))

# 하나씩 출력
for i in answer:
    print(*i)