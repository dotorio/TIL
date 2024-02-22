# import sys
# sys.stdin = open('input.txt')

# dec = ['0001101', '0011001', '0010011', '0111101', '0100011',
#        '0110001', '0101111', '0111011', '0110111', '0001011']

# pwd_ratio = [[3.0, 2.0, 1.0, 1.0], [2.0, 2.0, 2.0, 1.0], 
#              [2.0, 1.0, 2.0, 2.0], [1.0, 4.0, 1.0, 1.0],
#              [1.0, 1.0, 3.0, 2.0], [1.0, 2.0, 3.0, 1.0],
#              [1.0, 1.0, 1.0, 4.0], [1.0, 3.0, 1.0, 2.0],
#              [1.0, 2.0, 1.0, 3.0], [3.0, 1.0, 1.0, 2.0]]

# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]
#     visited = [[0]*M for _ in range(N)]
#     answer_sum = 0
#     i = 0
#     while i <= N-1:
#         for j in range(M-1, -1, -1):
#             if arr[i][j] != '0' and visited[i][j] == '0':
#                 password_0b = bin(int(arr[i][j], 16))[2:].zfill(4)
#                 last_x, last_y = i, j
#                 last_y -= 1
#                 for k in range(56):
#                     password_0b = password_0b + bin(int(arr[last_x][last_y], 16))[2:].zfill(4)
#                     last_y -= 1
print(len('FF8FC01C7E00E3F1F8FF8E00FC0FC0E07E070071F8'))
