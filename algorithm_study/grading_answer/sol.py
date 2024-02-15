import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    scores = []
    students = []
    answer = list(map(int, input().split()))
    for _ in range(N):
        students.append(list(map(int, input().split())))
    for student in students:
        score = 0
        correct = 0
        for i in range(M):
            if student[i] == answer[i]:
                correct += 1
                score += correct
            else:
                correct = 0
        scores.append(score)
    print(f'#{tc} {max(scores) - min(scores)}')