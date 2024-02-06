import sys
sys.stdin = open('GNS_test_input.txt')

number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

N = int(input())
# 테스트의 개수를 받는다
for case in range(1, N+1):
    # 각 테스트마다
    A, B = map(str, input().split())
    # 테스트 번호와 숫자의 개수를 받는다
    arr = []
    # 정렬할 리스트를 만든다.
    numbers = input().split()
    # 숫자들을 문자 형태로 numbers 리스트에 담는다
    for i in number:
        for j in numbers:
            if i == j:
                arr.append(i)
    # 각 넘버마다 numbers 리스트를 순회하며 같은 문자들을 정렬할 리스트에 담는다.
    print(A)
    print(*arr)
    # 테스트 번호와 정렬한 리스트를 출력한다
        
