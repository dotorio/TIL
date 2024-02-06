from itertools import combinations

A, B = map(int, input().split())
arr = list(map(int, input().split()))
combi = list(combinations(arr, 3))
sum_list = [sum(i) for i in combi if sum(i)<= B]
print(max(sum_list))
