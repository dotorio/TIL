N = int(input())
time = [False]*(10**9+1)
for _ in range(N):
    s, e = map(int, input().split())
    for i in range(s, e):
        if not time[i]:
            time[i] = 1
        else:
            time[i] += 1
print(sorted(time)[-1])