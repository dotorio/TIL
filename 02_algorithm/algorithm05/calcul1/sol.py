import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = input()
    formula = input()
    num_for = []
    for i in formula:
        if i.isdigit():
            num_for.append(int(i))
    print(f'#{tc} {sum(num_for)}')