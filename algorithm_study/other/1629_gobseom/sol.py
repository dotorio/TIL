A, B, C = map(int, input().split())
stack = [[1, A]]

while stack[-1][0] <= B:
    stack.append([stack[-1][0] * 2, stack[-1][1] ** 2])
print(stack)
