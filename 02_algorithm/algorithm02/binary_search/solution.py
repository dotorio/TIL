import sys
sys.stdin = open('sample_input.txt')

def find_P(book, page):
    cnt = 0
    standard = 0
    while book != page:
        cnt += 1
        if standard < page:
            standard = (book - standard) // 2
        elif standard > page:
            book = (book - standard) // 2
    return cnt

T = int(input())

for case in range(1, T + 1):
    P, A, B = map(int, input().split())
    cnt_A = 0
    cnt_B = 0
    if find_P(P, A) > find_P(P, B):
        print(f'#{case} A')
    elif find_P(P, A) < find_P(P, B):
        print(f'#{case} B')
    else:
        print(f'#{case} 0')
