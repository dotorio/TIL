import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
# 양수(or 0)리스트, 음수 리스트를 만들고 체크포인트를 담는다
arr_plus, arr_minus = [], []
for i in range(N):
    num = int(input())
    if num >= 0:
        arr_plus.append(num)
    else:
        arr_minus.append(-num)
# 리스트를 내림차순으로 정렬
arr_plus.sort(reverse=True)
arr_minus.sort(reverse=True)
# K 간격으로 리스트를 순회하면서
# 리스트 값 * 2 (오고 가는 거리) 만큼 answer에 더한다
answer = 0
for i in range(0, len(arr_plus), K):
    answer += arr_plus[i]*2
for i in range(0, len(arr_minus), K):
    answer += arr_minus[i]*2
print(answer)
