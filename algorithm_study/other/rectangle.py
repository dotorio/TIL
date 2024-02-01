for _ in range(4):
    arr = list(map(int, input().split()))

    rec_width = max(arr[2], arr[6])-min(arr[0], arr[4])
    rec_length = max(arr[3], arr[7])-min(arr[1], arr[5])
    sum_area = [[0]*(rec_width+1) for _ in range(rec_length+1)]
    new_x1 = arr[0] - min(arr[0], arr[4])
    new_y1 = arr[1] - min(arr[1], arr[5])
    new_x2 = arr[2] - min(arr[0], arr[4])
    new_y2 = arr[3] - min(arr[1], arr[5])
    new_x3 = arr[4] - min(arr[0], arr[4])
    new_y3 = arr[5] - min(arr[1], arr[5])
    new_x4 = arr[6] - min(arr[0], arr[4])
    new_y4 = arr[7] - min(arr[1], arr[5])
    for i in range(new_y1, new_y2):
        for j in range(new_x1, new_x2):
            sum_area[i][j] += 1
    for i in range(new_y3, new_y4):
        for j in range(new_x3, new_x4):
            sum_area[i][j] += 1
        if sum_area[i][j] == 2:
            print('a')
            break
    else:
        for i in range(new_y1, new_y2 + 1):
            sum_area[i][new_x2] += 1
        for j in range(new_x1, new_x2):
            sum_area[new_y2][j] += 1
        for i in range(new_y3, new_y4 + 1):
            sum_area[i][new_x4] += 1
        for j in range(new_x3, new_x4):
            sum_area[new_y4][j] += 1
        count_2 = 0
        for i in sum_area:
            count_2 += i.count(2)
            if count_2 > 1:
                print('b')
                break
        if count_2 == 0:
            print('d')
        elif count_2 == 1:
            print('c')

