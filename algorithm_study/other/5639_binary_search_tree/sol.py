# 재귀의 깊이가 깊기 때문에 리미트를 올려서 리커전에러를 막는다
import sys
sys.setrecursionlimit(10**5)

# 노드의 개수가 처음에 주어지지 않기 때문에
# try except로 노드를 받아서 저장한다
nums = []
while True:
    try:
        nums.append(int(input()))
    except EOFError:
        break
    
# tree 모형을 만들어둔다
tree = dict()
for i in nums:
    tree[i] = [0, 0]

# tree를 완성하는 함수    
def create_tree(par, son):
    
    # 만약 부모가 자식보다 크다면
    if par > son:
        
        # 왼쪽 자식이 있다면 그 왼쪽 자식을 부모로 함수 호출
        if tree[par][0]:
            create_tree(tree[par][0], son)
            
        # 왼쪽 자식이 없다면 son으로 채운다
        else:
            tree[par][0] = son
            
    # 만약 부모가 자식보다 작다면
    else:
        
        # 오른쪽 자식이 있다면 그 오른쪽 자식을 부모로 함수 호출
        if tree[par][1]:
            create_tree(tree[par][1], son)
            
        # 오른쪽 자식이 없다면 son으로 채운다
        else:
            tree[par][1] = son

# 노드들을 함수 안에 넣으면서 tree를 완성한다        
for i in range(1, len(nums)):
    
    # 첫번째 인자는 부모, 두번째 인자는 자식
    create_tree(nums[0], nums[i])

# 후위 순회하는 함수
def postorder(num):
    
    # 왼쪽 자식이 있다면 왼쪽 자식 순회
    if tree[num][0]:
        postorder(tree[num][0])
        
    # 오른쪽 자식이 있다면 오른쪽 자식 순회
    if tree[num][1]:
        postorder(tree[num][1])
        
    # 부모 출력
    print(num)

# 후위 순회하여 출력한다
postorder(nums[0])