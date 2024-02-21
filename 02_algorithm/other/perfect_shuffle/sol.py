import sys
sys.stdin = open('input.txt')
from collections import deque

for tc in range(1, int(input())+1):
    N = int(input())
    card = deque(input().split())
    card_left = card[:(N+1)//2]
    card_right = card[(N+1)//2:]
    