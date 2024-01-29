paper_num = int(input())
arr = [[0 for j in range(1001)] for i in range(1001)]
for i in range(paper_num):
    start_x, start_y, width, length = map(int, input().split())
    for x in range(width):
        for y in range(length):
            arr[start_y + y][start_x + x] = i + 1
for i in range(paper_num):
    count = 0
    for z in range(1001):
        count += arr[z].count(i + 1)
    print(count)