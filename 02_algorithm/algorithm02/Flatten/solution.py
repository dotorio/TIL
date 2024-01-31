import sys
sys.stdin = open('input.txt')

for case in range(1, 11):
    # 각 테스트마다
    dump = int(input())
    # 덤프 횟수를 받는다.
    box_list = list(map(int, input().split()))
    # 상자 높이들을 리스트로 받는다.
    for i in range(dump):
        # 덤프를 할 때마다
        the_max = box_list.index(max(box_list))
        the_min = box_list.index(min(box_list))
        # 가장 높은 높이의 리스트 인덱스 값을 the_max로 지정하고
        # 가장 낮은 높이의 리스트 인덱스 값을 the_min로 지정한다
        box_list[the_max] -= 1
        box_list[the_min] += 1
        # 상자 높이 리스트의 the_max 인덱스에 대응하는 값을 1 빼고
        # 상자 높이 리스트의 the_min 인덱스에 대응하는 값을 1 더한다

    result = max(box_list) - min(box_list)
    # 덤프를 모두 끝내면 상자 높이의 max값에 min값을 빼고 출력한다.
    print(f'#{case} {result}')