import sys
sys.stdin = open('input.txt')

for case in range(1, 11):
    length = int(input())
    arr = [list(map(str, input())) for i in range(8)]
    find = 0
    for i in arr:
        for j in range(8-length+1):
            word = i[j:j+length]
            if "".join(map(str,word)) == "".join(map(str,word[::-1])):
                find += 1
    arr = zip(*arr[::-1])
    for i in arr:
        for j in range(8-length+1):
            word = i[j:j+length]
            if "".join(map(str,word)) == "".join(map(str,word[::-1])):
                find += 1
    print(f'#{case} {find}')


