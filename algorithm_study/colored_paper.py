paper_num = int(input())
arr = [[0] * 1001 for _ in range(1001)]
# 1001 * 1001 배열을 만든다
for i in range(paper_num):
    start_x, start_y, width, length = map(int, input().split())
    for x in range(width):
        for y in range(length):
            arr[start_y + y][start_x + x] = i + 1
            # for문으로 색종이를 하나씩 덮는다.
for i in range(paper_num):
    count = sum(row.count(i + 1) for row in arr)
    print(count)
    # for문으로 배열 안의 색종이 넘버를 카운트해서 각각 넓이를 출력한다.
    
