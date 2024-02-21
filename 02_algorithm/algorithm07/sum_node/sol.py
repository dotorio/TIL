import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    # 트리로 만들 리스트
    tree = [0] * (N+1)
    # 리프 노드의 번호를 저장할 리스트
    leaf_node = []
    for i in range(M):
        node_num, num = map(int, input().split())
        # 트리에 리프 노드를 저장
        tree[node_num] = num
        # 리프 노드의 번호를 저장
        leaf_node.append(node_num)
    # 트리의 번호를 거꾸로 순회
    for i in range(N, 0, -1):
        # 해당 노드가 리프 노드라면 다음 순회로
        if i in leaf_node:
            continue
        # 리프 노드가 아니라면 자식 노드의 합으로 할당한다
        tree[i] = tree[2*i]
        if 2*i+1 <= N:
            tree[i] += tree[2*i+1]
    print(f'#{tc} {tree[L]}')