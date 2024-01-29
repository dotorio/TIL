sub_count = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
average = []
for sub_score in scores:
    average.append(sub_score/max_score*100)
print(sum(average)/len(average))
