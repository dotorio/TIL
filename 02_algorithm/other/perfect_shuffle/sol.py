import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, int(input())+1):
    N = int(input())
    card = list(input().split())
    card_left = deque(card[:(N+1)//2])
    card_right = deque(card[(N+1)//2:])
    print(f'#{tc}', end = ' ')
    while card_left:
        print(card_left.popleft(), end = ' ')
        if card_right:
            print(card_right.popleft(), end = ' ')
    print()
    