import sys
sys.stdin = open('input.txt')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

