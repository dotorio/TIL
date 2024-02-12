import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
sites = {}
for _ in range(N):
    site, pwd = input().split()
    sites[site] = pwd
for _ in range(M):
    print(sites[input()])