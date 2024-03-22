import sys
sys.stdin = open('input.txt')

N = int(input())
S, P = map(int, input().split())
team = []
for i in range(N):
    score1, per1, lang1, m1 = input().split()
    score1 = int(score1)
    per1 = int(per1)
    print(score1, per1, lang1, m1)
    score2, per2, lang2, m2 = input().split()
    score2 = int(score2)
    per2 = int(per2)
    print(score2, per2, lang2, m2)