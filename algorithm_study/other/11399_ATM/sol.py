import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
P.sort()
sum = 0
P_sum = 0
for i in P:
    sum += i
    P_sum += sum
print(P_sum)