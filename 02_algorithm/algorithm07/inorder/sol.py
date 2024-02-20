import sys
sys.stdin = open('input.txt')

def inorder(A):
    # A가 0이 아니라면
    if A:
        # 왼쪽 자식을 먼저 순회
        inorder(tree[A][0])
        # 자기 번호의 단어를 answer에 넣는다
        answer.append(word[A])
        # 오른쪽 자식을 순회
        inorder(tree[A][1])

for tc in range(1, 11):
    N = int(input())
    # 자식 노드를 인식시킬 리스트를 만든다
    tree = [[0,0] for _ in range(N+1)]
    # 단어를 넣을 리스트를 만든다
    word = [0] * (N+1)
    # 자식 노드 리스트와 단어 리스트를 완성한다
    for _ in range(N):
        node = list(input().split())
        word[int(node[0])] = node[1]
        if len(node) > 2:
            tree[int(node[0])][0] = int(node[2])
        if len(node) > 3:
            tree[int(node[0])][1] = int(node[3])
    # 출력할 단어를 모을 리스트를 만든다
    answer = []
    # 중위 순회 함수 호출
    inorder(1)
    print(f"#{tc} {''.join(answer)}")

