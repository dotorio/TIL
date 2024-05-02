# 중복조합 사용
from itertools import combinations_with_replacement

N, M = map(int, input().split())

# 숫자들을 오름차순 정렬해서 받는다
nums = sorted(list(map(int, input().split())))

# 중복조합을 적용한 리스트를 생성한다
data = combinations_with_replacement(nums, M)

# 하나씩 출력하면 끝
for i in data:
    print(" ".join(map(str, i)))