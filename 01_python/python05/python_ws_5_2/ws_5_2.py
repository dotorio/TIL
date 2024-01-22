# 아래 함수를 수정하시오.
def remove_duplicates(x):
    y = set(x)
    z = list(y)
    new_lst = []
    new_lst.extend(z)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
