import sys
sys.stdin = open('input.txt')

K = int(input())
square = {'W' : [], 'H' : []}
max_w, max_h, w_max_idx, h_max_idx = 0,0,0,0
for i in range(6):
    drc, length = map(int, input().split())
    if i % 2 == 0:
        square['W'].append([length, i])
        if max_w < length:
            max_w = length
            w_max_idx = i
    else:
        square['H'].append([length, i])
        if max_h < length:
            max_h = length
            h_max_idx = i
if abs(w_max_idx - h_max_idx) == 1:
    min_idx1 = (max(w_max_idx, h_max_idx) + 2) % 6
    min_idx2 = (min_idx1 + 1) % 6
else:
    min_idx1 = 2
    min_idx2 = 3
for i in square['W']:
    if i[1] == min_idx1:
        min_w = i[0]
    elif i[1] == min_idx2:
        min_w = i[0]
for i in square['H']:
    if i[1] == min_idx1:
        min_h = i[0]
    elif i[1] == min_idx2:
        min_h = i[0]

print((max_w * max_h - min_w * min_h) * K)

    