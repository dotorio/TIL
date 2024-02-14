import sys
sys.stdin = open('input.txt')

def f(i, k, s):
    global min_v
    # 배열을 모두 순회했을 때 고른 숫자들의 합이 최솟값보다 작다면
    # 최솟값을 갱신한다
    if i == k:
        if min_v > s:
            min_v = s          
        return
    # 배열을 모두 순회하지 않았지만 고른 숫자들의 합이 최솟값보다 크다면
    # 의미없는 순회를 멈춘다
    elif s > min_v:
        return
    # 배열을 모두 순회하지 않고 고른 숫자들의 합이 최솟값보다 작아서
    # 계속 순회가 필요하다면
    else:
        # 다른 원소와 자리를 바꾸며 순열을 만들어가고
        for j in range(i, k):
            P[i], P[j] = P[j], P[i]
            # 숫자를 골라 합에 더한다
            f(i+1, k, s + arr[i][P[i]])
            # 마지막엔 P를 원상복구
            P[j], P[i] = P[i], P[j]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 순열 생성에 필요한 리스트를 만든다
    P = list(range(N))
    # 최솟값을 100으로 설정해둔다
    min_v = 100
    # 순열에 사용할 번호, 배열의 크기, 고른 숫자들의 합을 변수로 함수를 호출한다
    f(0, N, 0)
    # 함수를 거쳐 나온 최솟값을 출력한다
    print(f'#{tc} {min_v}')
