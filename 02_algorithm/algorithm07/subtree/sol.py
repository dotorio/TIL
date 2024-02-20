import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    # 자식 노드를 등록할 리스트를 2개 만든다
    sub1 = [0]*(E+2)
    sub2 = [0]*(E+2)
    # 자식 노드를 등록한다
    for i in range(E):
        if sub1[tree[2*i]] == 0:
            sub1[tree[2*i]] = tree[2*i+1]
        else:
            sub2[tree[2*i]] = tree[2*i+1]
    # 시작할 노드를 스택에 넣고 cnt는 1로 시작한다
    stack = [N]
    cnt = 1
    # 스택이 빌 때까지 자손 노드를 찾고 cnt를 올린다
    while stack:
        now = stack.pop()
        if sub1[now] != 0:
            stack.append(sub1[now])
            cnt +=1
        if sub2[now] != 0:
            stack.append(sub2[now])
            cnt +=1
    print(f'#{tc} {cnt}')