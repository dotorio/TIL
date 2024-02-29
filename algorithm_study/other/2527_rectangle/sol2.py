# 각 테스트케이스에 대해서
for tc in range(1, int(input())+1):
    # 두 직사각형의 정보를 받아서
    recs = list(map(int, input().split()))
    # 첫번째 직사각형의 가로 범위를 세트로 만듬
    range1 = set(range(recs[0], recs[2]+1))
    # 첫번째 직사각형의 세로 범위를 세트로 만듬
    range2 = set(range(recs[1], recs[3]+1))
    # 두번째 직사각형의 가로 범위를 세트로 만듬
    range3 = set(range(recs[4], recs[6]+1))
    # 두번째 직사각형의 세로 범위를 세트로 만듬
    range4 = set(range(recs[5], recs[7]+1))
    # 만약 두 직사각형의 가로 범위가 겹치지 않거나 세로 범위가 겹치지 않으면
    # 두 직사각형은 만나지 않는 것이므로
    if range1 & range3 == set() or range2 & range4 == set():
        # 4번 상태를 출력
        print(f'#{tc} 4')
    # 만약 두 직사각형의 가로, 세로 범위가 모두 1개씩 겹치면
    # 두 직사각형은 한 점에서 만나는 것이므로
    elif len(range1 & range3) == 1 and len(range2 & range4) == 1:
        # 3번 상태를 출력
        print(f'#{tc} 3')
    # 만약 두 직사각형의 가로, 세로 범위가 모두 2 이상씩 겹치면
    # 두 직사각형은 겹치는 넓이가 있는 것이므로
    elif len(range1 & range3) > 1 and len(range2 & range4) > 1:
        # 1번 상태를 출력
        print(f'#{tc} 1')
    # 위 3가지 경우가 모두 아니라면
    else:
        # 2번 상태를 출력
        print(f'#{tc} 2')