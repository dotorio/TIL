import sys
sys.stdin = open('input.txt')

# i, j 인덱스에 해당하는 공장 제품 생산
# arr는 순열에 사용할 배열
# now_cost는 현재까지 더한 비용
def f(i, j, arr, now_cost):
    global min_cost
    # 만약 현재까지 더한 비용이 이미 최소 생산 비용을 넘었다면
    if now_cost >= min_cost:
        # 즉시 손절
        return
    # 해당 인덱스의 공장의 제품 비용을 더해준다
    now_cost += cost[i][j]
    # 마지막 공장까지 돌았다면
    if i == N-1:
        # 최소 생산 비용을 갱신하고 리턴
        min_cost = min(min_cost, now_cost)
        return
    # 방금 더한 j의 인덱스를 기억한다
    idx = arr.index(j)
    # j를 arr에서 지우고
    arr.remove(j)
    # 남은 arr만큼 함수 호출
    for k in arr:
        f(i+1, k, arr, now_cost)
    # 다시 j를 arr에 더한다(백트래킹)
    arr.insert(idx, j)
    

for tc in range(1, int(input())+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    # 최소 생산 비용을 1500으로 설정
    min_cost = 1500
    # 첫번째 공장이 만들 제품을 정해주고 함수 호출
    for j in range(N):
        arr = list(range(N))
        f(0, j, arr, 0)
    # 완성된 최소 생산 비용을 출력
    print(f'#{tc} {min_cost}')