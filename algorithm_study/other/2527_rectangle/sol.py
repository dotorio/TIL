import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(4):
    recs = list(map(int, input().split()))
    range1 = set(range(recs[0], recs[2]+1))
    range2 = set(range(recs[1], recs[3]+1))
    range3 = set(range(recs[4], recs[6]+1))
    range4 = set(range(recs[5], recs[7]+1))
    if range1 & range3 == set() or range2 & range4 == set():
        print('d')
    elif len(range1 & range3) == 1 and len(range2 & range4) == 1:
        print('c')
    elif len(range1 & range3) > 1 and len(range2 & range4) > 1:
        print('a')
    else:
        print('b')