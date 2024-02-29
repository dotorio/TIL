N, r, c = map(int, input().split())

def visit(a, b, c, d, num1, num2, vst):
    if c - a == 2:
        cnt = 1
        for i in range(2):
            for j in range(2):
                if a+i == num1 and b+j == num2:
                    return vst+cnt
                cnt += 1
    else:
        if a <= r < c-(c-a)//2 and b
len_arr = 2 ** N
print(visit(0, 0, len_arr, len_arr, r, c, 0))