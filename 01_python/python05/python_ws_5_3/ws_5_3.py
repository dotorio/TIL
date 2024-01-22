# 아래 함수를 수정하시오.
def sort_tuple(x):
    y = list(x)
    y.sort()
    new_tuple = tuple(y)

    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
