import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    # 양의 정수 or 연산자를 저장할 트리
    tree = [0]*(N+1)
    # 자식 정보를 저장할 리스트
    son = [[] for _ in range(N+1)]
    # 트리와 리스트를 완성
    for _ in range(N):
        node = list(input().split())
        tree[int(node[0])] = node[1]
        if len(node) == 4:
            son[int(node[0])] = [int(node[2]), int(node[3])]
    # 노드 번호를 거꾸로 순회하며
    for i in range(N, 0, -1):
        # 노드가 양의 정수라면 다음 순회로
        if tree[i].isdigit():
            continue
        # 노드가 연산자라면 자식 정보와 연동해서 계산해서
        # 트리 정보를 갱신한다
        if tree[i] == '+':
            tree[i] = int(tree[son[i][0]]) + int(tree[son[i][1]])
        elif tree[i] == '-':
            tree[i] = int(tree[son[i][0]]) - int(tree[son[i][1]])
        elif tree[i] == '*':
            tree[i] = int(tree[son[i][0]]) * int(tree[son[i][1]])
        else:
            tree[i] = int(tree[son[i][0]]) / int(tree[son[i][1]])
    print(f'#{tc} {int(tree[1])}')