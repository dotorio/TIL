N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
list_sum = 0
for _ in range(N):
    list_sum += A[_] * B[-_-1]
print(list_sum)