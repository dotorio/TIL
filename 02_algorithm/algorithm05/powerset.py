def powerset(K, result, cnt):
    if K == N:
        if cnt == 10:
            print(result)
        return
    else:
        powerset(K+1, result + [arr[K]], cnt + arr[K])
        powerset(K+1, result, cnt)

N = 10
arr = list(range(1, 11))
powerset(0, [], 0)
