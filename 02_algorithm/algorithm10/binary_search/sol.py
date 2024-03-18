import sys
sys.stdin = open('input.txt')

def bs(i, low, high, dir):
    global cnt
    # 찾지 못햇으면 리턴
    if low > high:
        return
    else:
        mid = (low + high) // 2
        # 중간값이라면 cnt를 1 더함
        if i == A[mid]:
            cnt += 1
        # 중간값보다 작고 방향이 오른쪽이었다면
        elif i < A[mid] and dir:
            # 왼쪽으로 함수 호출
            bs(i, low, mid-1, 0)
        # 중간값보다 크고 방향이 왼쪽이었다면
        elif i > A[mid] and not dir:
            # 오른쪽으로 함수 호출
            bs(i, mid+1, high, 1)

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    # B에 있는 원소에 대해 탐색 시작
    for i in B:
        # 중간값이라면 cnt를 1 더함
        if i == A[(N-1)//2]:
            cnt += 1
        # 중간값보다 크다면 함수 호출(1은 오른쪽, 0은 왼쪽)
        elif i > A[(N-1)//2]:
            bs(i, (N-1)//2+1, N-1, 1)
        # 중간값보다 작다면 함수 호출
        else:
            bs(i, 0, (N-1)//2-1, 0)   
    print(f'#{tc} {cnt}')