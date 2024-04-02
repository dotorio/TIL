N = list(input())
# 10의 배수 체크
if '0' not in N:
    print(-1)
# 3의 배수 체크
elif sum(map(int, N))%3:
    print(-1)
# else로 왔다면 30의 배수가 있다
else:
    N.sort(reverse=True)
    print(''.join(N))