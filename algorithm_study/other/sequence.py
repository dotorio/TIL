# N = int(input())
# seq = list(map(int, input().split()))
# max_length = 1
# for i in range(N):
#     seq_length = 1
#     k = i
#     while k+1 < N and seq[k] <= seq[k+1]:
#         seq_length += 1
#         k = k+1
#     if max_length < seq_length:
#         max_length = seq_length
#     seq_length = 1
#     k = i
#     while k+1 < N and seq[k] >= seq[k+1]:
#         seq_length += 1
#         k = k+1
#     if max_length < seq_length:
#         max_length = seq_length
#     k = i
# print(max_length)

N = int(input())
seq = list(map(int, input().split()))
max_length = 1
i = 0
while i < N:
    seq_length = 1
    while i+1 < N and seq[i] <= seq[i+1]:
        seq_length += 1
        i = i+1
    max_length = max(max_length, seq_length)
    i = i+1
i = 0
while i < N:
    seq_length = 1
    while i+1 < N and seq[i] >= seq[i+1]:
        seq_length += 1
        i = i+1
    max_length = max(max_length, seq_length)
    i = i+1
print(max_length)

# N = int(input())
# seq = list(map(int, input().split()))
# max_length = 1

# def find_max_length(start, end, step):
#     global max_length
#     seq_length = 1
#     for i in range(start, end, step):
#         while i + 1 < end and seq[i] <= seq[i + 1]:
#             seq_length += 1
#             i += 1
#         max_length = max(max_length, seq_length)
#         seq_length = 1

# for i in range(N):
#     find_max_length(i, N, 1)  # increasing sequence
#     find_max_length(i, N, -1)  # decreasing sequence

# print(max_length)

