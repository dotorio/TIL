import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
end = sorted(numbers)
stack = []
snack = []
for i in range(1, N+1):
    while i not in snack:
        if len(stack) != 0 and stack[-1] == i:
            snack.append(stack.pop())
        else:
            if len(numbers) == 0:
                break
            now = numbers.pop(0)
            if now != i:
                stack.append(now)
            else:
                snack.append(now)
if snack == end:
    print('Nice')
else:
    print('Sad')