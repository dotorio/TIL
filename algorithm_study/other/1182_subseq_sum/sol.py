N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

def powerset(K, result, cnt):
    global count
    if K == N:
        if result != [] and cnt == S:
            count += 1
        return
    else:
        powerset(K+1, result + [nums[K]], cnt + nums[K])
        powerset(K+1, result, cnt)

powerset(0, [], 0)
print(count)