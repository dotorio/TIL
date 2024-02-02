arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
bingo_arr = [[0] * 5 for _ in range(5)]
cnt = 0

def bingo(arr):
    if sum(arr[i][i] for i in range(5)) == 5:
        return True
    if sum(arr[4-i][i] for i in range(5)) == 5:
        return True
    for i in range(5):
        if sum(arr[i]) == 5:
            return True
    for i in range(5):
        row_sum = 0
        for j in range(5):
            row_sum += arr[j][i]
        if row_sum == 5:
            return True    
    return False

for i in range(5):
    for j in range(5):
        for i2 in range(5):
            for j2 in range(5):
                if arr[i2][j2] == arr2[i][j]:
                    bingo_arr[i2][j2] = 1
                    cnt += 1
                    if bingo(bingo_arr) == True:
                        print(cnt)
                        break
                    break
            if bingo(bingo_arr) == True:
                break
        if bingo(bingo_arr) == True:
            break
    if bingo(bingo_arr) == True:
        break

            

