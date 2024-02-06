import sys
sys.stdin = open('input.txt')

T = int(input())
test = list(range(1, 10))
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for i in range(9)]
    case = True
    # 가로 행을 검사
    for i in sudoku:
        new = sorted(i)
        if new != test:
            case = False
            print(f'#{tc} 0')
            break
    sudoku = list(zip(*sudoku))
    # 세로 열을 검사
    for i in sudoku:
        if case == False:
            break
        new = sorted(i)
        if new != test:
            case = False
            print(f'#{tc} 0')
            break
        # 3 * 3 행렬을 검사
    for i in range(0,7,3):
        if case == False:
            break
        for j in range(0,7,3):
            new = []
            new.extend(sudoku[i][j:j+3])
            new.extend(sudoku[i+1][j:j+3])
            new.extend(sudoku[i+2][j:j+3])
            new.sort()
            if new != test:
                case = False
                print(f'#{tc} 0')
                break
    if case == True:
        print(f'#{tc} 1')