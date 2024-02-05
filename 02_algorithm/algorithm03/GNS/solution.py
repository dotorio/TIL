import sys
sys.stdin = open('GNS_test_input.txt')

number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

N = int(input())
for case in range(1, N+1):
    A, B = map(str, input().split())
    arr = []
    numbers = list(map(str, input().split()))
    for i in number:
        for j in numbers:
            if i == j:
                arr.append(i)
    print(A)
    print(" ".join(arr))
        
