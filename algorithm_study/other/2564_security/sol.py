import sys
sys.stdin = open('input.txt')

W, H = map(int, input().split())
sum = 0
N = int(input())
store = [list(map(int, input().split())) for _ in range(N)]
man = list(map(int, input().split()))
for i in store:
    if [man[0], i[0]] in [[1,3], [3,1]]:
        sum += man[1] + i[1]
    elif [man[0], i[0]] in [[1,2], [2,1]]:
        sum += min(H + man[1] + i[1], H + (W-man[1]) + (W-i[1]))
    elif [man[0], i[0]] in [[3,4], [4,3]]:
        sum += min(W + man[1] + i[1], W + (H-man[1]) + (H-i[1]))
    elif [man[0], i[0]] == [1,4]:
        sum += W-man[1] + i[1]
    elif [man[0], i[0]] == [4,1]:
        sum += man[1] + W-i[1]
    elif [man[0], i[0]] == [3,2]:
        sum += H-man[1] + i[1]
    elif [man[0], i[0]] == [2,3]:
        sum += man[1] + H-i[1]
    elif [man[0], i[0]] == [2,4]:
        sum += W-man[1] + H-i[1]
    elif [man[0], i[0]] == [4,2]:
        sum += H-man[1] + W-i[1]
    else:
        sum += abs(man[1] - i[1])
print(sum)
