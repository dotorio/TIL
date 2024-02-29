import sys
sys.stdin = open('input.txt')

N = int(input())
stack1, stack2, stack3, stack4 = [], [], [], []
num = list(map(int, input().split()))
result = True
for i in range(N):
    if not stack1 or stack1[-1] < num[i]:
        stack1.append(num[i])
    elif not stack2 or stack2[-1] < num[i]:
        stack2.append(num[i])
    elif not stack3 or stack3[-1] < num[i]:
        stack3.append(num[i])
    elif not stack4 or stack4[-1] < num[i]:
        stack4.append(num[i])
    else:
        result = False
        print('NO')
        break
if result:
    print('YES')
