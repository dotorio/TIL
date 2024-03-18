import sys
sys.stdin = open('input.txt')

def f(tower, idx):
    global min_tower
    # 직원을 끝까지 순회했거나
    # 최소 탑의 높이가 B와 같아서 더 순회할 필요가 없다면
    if idx == N or min_tower == B:
        # 세워진 탑의 높이가 조건에 맞다면
        if B <= tower < min_tower:
            # 최소 탑의 높이를 갱신
            min_tower = tower
        return
    # 아직 탑의 높이가 B보다 작다면
    if tower < B:
        # 해당 직원을 사용할 때와
        # 사용하지 않을 때를 모두 호출
        f(tower + clerk[idx], idx+1)
        f(tower, idx+1)
    # 지금까지 세워진 탑의 높이가 조건에 맞다면
    elif B <= tower < min_tower:
        # 최소 탑의 높이를 갱신
        min_tower = tower
        return

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))
    # 세울 탑의 높이를 0으로, 최소 탑의 높이를 200000으로 설정
    tower, min_tower = 0, 200000
    f(tower, 0)
    print(f'#{tc} {min_tower - B}')