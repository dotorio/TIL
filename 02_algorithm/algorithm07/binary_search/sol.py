import sys
sys.stdin = open('input.txt')

def inorder(A):
    global cnt, node, root
    # 해당 노드가 0이 아니라면
    if A:
        # 왼쪽 자식부터 순회
        inorder(tree[A][0])
        # cnt는 해당 위치에 저장된 값
        cnt += 1
        # 해당 노드가 N/2번 노드라면 변수에 할당
        if A == N//2 and node == 0:
            node = cnt
        # 해당 노드가 루트 노드라면 변수에 할당
        if par[A] == 0 and root == 0:
            root = cnt
        # 오른쪽 자식을 순회
        inorder(tree[A][1])
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 자식 노드를 인식시킬 리스트를 만든다
    tree = [[0,0] for _ in range(N+1)] 
    # 부모 노드를 인식시킬 리스트를 만든다
    par = [0] * (N+1)
    # cnt를 올리면서 리스트를 완성시킬 것이다
    cnt = 1
    # 자식 노드 리스트, 부모 노드 리스트를 완성시킨다
    while cnt*2 <= N:
        tree[cnt][0] = cnt*2
        par[cnt*2] = cnt
        if cnt*2+1 <= N:
            tree[cnt][1] = cnt*2+1
            par[cnt*2+1] = cnt
        cnt +=1
    # 루트와 노드에 저장할 값을 함수 속에서 cnt로 알아낼 것이다
    cnt = 0
    node = 0
    root = 0
    # 중위 순회 함수 호출
    inorder(1)
    print(f'#{tc} {root} {node}')
        