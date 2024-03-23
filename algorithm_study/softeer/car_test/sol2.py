import sys
sys.stdin = open('input.txt')

from bisect import bisect_left

# 중앙값 계산 함수
def count_median(car, mi):
    n = len(car)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                median = sorted([car[i], car[j], car[k]])[1]
                if median == mi:
                    count += 1
    return count

# 입력 받기
n, q = map(int, input().split())
car = sorted(list(map(int, input().split())))
expect = [int(input()) for _ in range(q)]

# 중앙값 계산 및 출력
for mi in expect:
    print(count_median(car, mi))