paper_cnt = int(input())
sum_area = set()
for number in range(paper_cnt):
    A, B = map(int, input().split())
    for i in range(A, A+10):
        for j in range(B, B+10):
            sum_area.add(1000 * i + j)
print(len(sum_area))