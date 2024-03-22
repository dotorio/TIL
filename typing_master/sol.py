import sys
sys.stdin = open('input.txt',  'rt', encoding='UTF8')
from itertools import permutations

def f(n):
    # 입력된 숫자를 문자열로 변환하여 각 자릿수를 분리
    digits = list(str(n))
    
    # 모든 자릿수의 순열을 구함
    perms = permutations(digits)
    
    # 각 순열을 문자열로 변환하여 출력
    for perm in perms:
        print(''.join(perm))

N = int(input())
S, P = map(int, input().split())
team = []
for i in range(N):
    score1, per1, lang1, m1 = input().split()
    score2, per2, lang2, m2 = input().split()
    team.append((int(score1), int(per1), lang1, m1, int(score2), int(per2), lang2, m2))

