N, K = map(int, input().split())
a = 1
b = 1
for i in range(K):
    a *= N-i
for i in range(K-1):
    b *= K-i
print(int(a/b))
# def factorial(a, b):
#         if b == 1:
#             return a
#         return a * factorial(a-1, b-1)
# def factorial_2(a):
#         if a == 1:
#             return 1
#         return a * factorial_2(a-1)
# print(int(factorial(N, K) / factorial_2(K)))