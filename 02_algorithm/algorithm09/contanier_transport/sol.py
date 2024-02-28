import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ctn = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    # 컨테이너와 트럭들을 내림차순으로 정렬
    ctn.sort(reverse=True)
    truck.sort(reverse=True)
    # 마지막에 출력할 무게를 0으로 설정
    sum = 0
    # 트럭, 컨테이너를 2중 순회
    for i in truck:
        for j in ctn:
            # 트럭에 실을 수 있는 컨테이너를 발견하면
            if i >= j:
                # 무게에 더하고
                sum += j
                # 트럭에 실었으므로 컨테이너에서 뺀다
                ctn.remove(j)
                # 다음 트럭을 순회하기 위해 break
                break
    # 테케와 무게를 출력한다
    print(f'#{tc} {sum}')

