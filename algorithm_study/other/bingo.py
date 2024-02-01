arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
cnt = 0

def bingo(num, y, x):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                arr[i][j] = 0
    one_length = 0
    while 
    return True


for i in range(5):
    for j in range(5):
        cnt += 1
        if bingo(arr2[i][j], i, j) == True:
            print(cnt)
            quit()
