N = int(input())
def my_round(n):
    if n - int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)
if N == 0:
    print(0)
else:
    arr = sorted(int(input()) for _ in range(N))
    length = my_round(N*0.15)
    new_arr = arr[length:N - length]
    print(my_round(sum(new_arr)/len(new_arr)))
