import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def tet(arr, N, M):
    global max_tet
    for j in range(N-1):
        for i in range(M-2):
            T1 = sum(arr[j][i:i+3]) + arr[j+1][i+1]
            if T1 > max_tet:
                max_tet = T1
            T2 = sum(arr[j+1][i:i+3]) + arr[j][i+1]
            if T2 > max_tet:
                max_tet = T2
            L1 = sum(arr[j][i:i+3]) + arr[j+1][i]
            if L1 > max_tet:
                max_tet = L1
            L2 = sum(arr[j+1][i:i+3]) + arr[j][i+2]
            if L2 > max_tet:
                max_tet = L2
    for j in range(N-2):
        for i in range(M-1):
            Z = sum(arr[j+1][i:i+2]) + arr[j][i+1] + arr[j+2][i]
            if Z > max_tet:
                max_tet = Z
            S = sum(arr[j+1][i:i+2]) + arr[j][i] + arr[j+2][i+1]
            if S > max_tet:
                max_tet = S
            J1 = sum(arr[j][i:i+2]) + arr[j+1][i] + arr[j+2][i]
            if J1 > max_tet:
                max_tet = J1
            J2 = sum(arr[j+2][i:i+2]) + arr[j][i+1] + arr[j+1][i+1]
            if J2 > max_tet:
                max_tet = J2
    for j in range(N):
        for i in range(M-3):
            straight = sum(arr[j][i:i+4])
            if straight > max_tet:
                max_tet = straight

N1, M1 = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N1)]
max_tet = 4
for j in range(N1-1):
    for i in range(M1-1):
        square = sum(arr[j][i:i+2]) + sum(arr[j+1][i:i+2])
        if square > max_tet:
            max_tet = square
tet(arr, N1, M1)
new_arr = list(zip(*arr[::-1]))
tet(new_arr, M1, N1)
print(max_tet)
