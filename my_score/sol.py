import sys
sys.stdin = open(('input.txt'))

N = int(input())
num_sum, sco_sum = 0, 0
for i in range(N):
    num, sco = map(int, input().split())
    num_sum += num
    sco_sum += sco*num
print(sco_sum/num_sum)