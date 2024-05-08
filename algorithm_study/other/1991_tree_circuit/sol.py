import sys
sys.stdin = open('input.txt')

# 왼쪽 자식은 left, 오른쪽 자식은 right에 기록
left, right = dict(), dict()
N = int(input())
for _ in range(N):
    par, left_son, right_son = input().split()
    if left_son != '.':
        left[par] = left_son
    if right_son != '.':
        right[par] = right_son

def tree(char):
    preorder, inorder, postorder = [], [], []

    # 전위 순회에 기록
    preorder.append(char)

    # 왼쪽 자식이 있다면
    if char in left:

        # 재귀로 리턴시켜 가져온 리스트들을 각각 합침
        next_preorder, next_inorder, next_postorder = tree(left[char])
        preorder.extend(next_preorder)
        inorder.extend(next_inorder)
        postorder.extend(next_postorder)

    # 중위 순회에 기록
    inorder.append(char)

    # 오른쪽 자식이 있다면
    if char in right:

        # 재귀로 리턴시켜 가져온 리스트들을 각각 합침
        next_preorder, next_inorder, next_postorder = tree(right[char])
        preorder.extend(next_preorder)
        inorder.extend(next_inorder)
        postorder.extend(next_postorder)

    # 후위 순회에 기록
    postorder.append(char)

    # 완성된 세 리스트들을 리턴
    return preorder, inorder, postorder

# 함수를 호출시켜 세 리스트들을 완성시킴
preorder, inorder, postorder = tree('A')

print(''.join(preorder))
print(''.join(inorder))
print(''.join(postorder))
