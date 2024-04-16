from itertools import permutations

N, K = map(int, input().split())
kits = list(map(int, input().split()))

# 출력할 결과를 0으로 놓고
result = 0

# 순열을 이용해 플랜들을 만들어서 순회
for plan in list(permutations(kits, N)):

    # 플랜 안 운동 키트를 더하고 K를 뺐을 때
    # 근손실이 일어나면 break
    start = 0
    for kit in plan:
        start += kit - K
        if start < 0:
            break

    # 끝까지 근손실이 일어나지 않으면 결과에 1 더함
    else:
        result += 1

# 완성된 결과를 출력
print(result)
        