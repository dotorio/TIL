N = int(input())

if N in [4, 7]:
    print(-1)
elif N % 5 in [2, 4]:
    print(N//5+2)
elif N % 5 in [1, 3]:
    print(N//5+1)
else:
    print(N//5)