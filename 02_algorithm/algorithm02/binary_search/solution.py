import sys
sys.stdin = open('sample_input.txt')

# 함수의 정의는 함수 호출 시에 올라와서 볼 것
def find_P(book, page):
    # 함수의 변수는 책의 전체 페이지 수, 찾을 페이지를 받는다.
    arr = list(range(book))
    # 책의 전체 페이지를 range로 전체 리스트로 만든다.
    cnt = 0
    # 탐색 횟수를 0으로 설정
    start = 0
    end = book-1
    # 탐색을 시작할 첫 페이지를 0, 마지막 페이지를 마지막 페이지 -1로 설정한다
    # 배열의 index에 맞추기 위해서임
    while start <= end:
        middle = (start + end) // 2
        # 탐색을 시작하면 첫 페이지와 마지막 페이지의 중간을 미들로 설정
        cnt += 1
        # 탐색 횟수를 1 더한다.
        if arr[middle] > page-1:
            # 찾는 페이지가 미들보다 작을 경우
            end = middle
            # 다음 탐색 때 마지막 페이지를 미들로 설정한다
        elif arr[middle] < page-1:
            # 찾는 페이지가 미들보다 클 경우
            start = middle
            # 다음 탐색 때 첫 페이지를 미들로 설정한다
        else:
            return cnt
    return cnt
    # 탐색할 페이지를 찾았다면 탐색 횟수를 반환한다.

T = int(input())
# 테스트 개수를 받는다.

for case in range(1, T + 1):
    # 각 테스트마다
    P, A, B = map(int, input().split())
    # 책의 페이지 수, A가 찾을 페이지, B가 찾을 페이지를 받는다
    if find_P(P, A) < find_P(P, B):
        print(f'#{case} A')
        # A가 더 빨리 찾았다면 A를 출력
    elif find_P(P, A) > find_P(P, B):
        print(f'#{case} B')
        # B가 더 빨리 찾았다면 B를 출력
    else:
        print(f'#{case} 0')
    # 둘다 아니면 0을 출력
