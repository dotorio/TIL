import sys
sys.stdin = open('input.txt')

n, q = map(int, input().split())
# 차들의 연비를 오름차순 정렬된 리스트로 만듬 
car = sorted(list(map(int, input().split())))
# expect 리스트를 만들어 중앙값들을 넣는다
expect = []
for i in range(q):
    # 첫번째 인자는 중앙값
    # 두번째 인자는 나중에 할당할 가짓수(디폴트는 0)
    # 세번째 인자는 마지막에 정렬할 기준 인덱스
    expect.append([int(input()), 0, i])
# 리스트를 오름차순 정렬한다
expect.sort()
# i는 car를 순회할 인덱스
# j는 expect를 순회할 인덱스
i, j = 0, 0
# car나 expect 둘 중 하나를 다 순회하면 종료
while i != n and j != q:
    # 만약 해당 연비와 중앙값이 같다면
    if car[i] == expect[j][0]:
        # 중앙값의 가짓수를 할당한다
        expect[j][1] = i*(n-i-1)
        # 다음 expect 원소를 순회
        # car는 아직 순회하지 않는다
        # 이유는 다음 expect 원소값이 현재 car 원소값과 같을 수 있기 때문
        j += 1
    # 만약 해당 연비가 중앙값보다 크다면
    elif car[i] > expect[j][0]:
        # 다음 expect 원소를 순회
        j += 1
    # 만약 해당 연비보다 중앙값이 크다면
    else:
        # 다음 car를 순회
        i += 1
# 최초의 인덱스를 기준으로 정렬해서        
expect.sort(key=lambda x: x[2])
# 중앙값의 가짓수를 출력
for i in expect:
    print(i[1])
    