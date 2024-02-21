import sys
sys.stdin = open('input.txt')

# 최소 힙
def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지)
    h[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모 < 자식 비교를 위해
    p = c // 2  # 부모번호 계산
    while p >= 1 and h[p] > h[c]:   # 부모가 있는데, 그 부모가 더 크면
        h[p], h[c] = h[c], h[p]     # 자리를 바꾼다
        c = p
        p = c // 2

for tc in range(1, int(input())+1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 최소 힙을 위한 리스트 만들기
    h = [0] * (N+1)
    last = 0
    # 숫자를 순서대로 최소 힙에 넣는다
    for num in nums:
        enq(num)
    # 출력할 정수의 합을 0으로 설정
    sum = 0
    # 마지막 노드의 조상 노드 인덱스를 설정
    c = N // 2
    # 루트 노드까지 올라가면서 조상 노드에 저장된 정수를 sum에 더한다
    while c != 0:
        sum += h[c]
        c //= 2
    print(f'#{tc} {sum}')
