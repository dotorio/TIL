import math
N = int(input())
arr = list(map(int, input().split()))
prime = 0
for i in arr:
    for j in range(2, int(math.sqrt(i))+2):
        while i == 1 or i % j == 0:
            break
    while i == 1 or i % j == 0:
        break
    else:
        prime += 1
print(prime)

# s1 = 'abc'
# s2 = 'abc'
# s3 = 'def'
# s4 = s1
# s5 = s1[:2] + 'c'
# print(s1 is s2)