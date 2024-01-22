# 아래 함수를 수정하시오.
def find_min_max(arr):
    arr.sort()
    return arr[0], arr[-1]

def find_min_max_2(arr):
    return min(arr), max(arr)

def find_max(arr):
    result = 0
    for num in arr:
        if result < num:
            result = num
    return result

def find_min(arr):
    result = arr[0]
    for num in arr:
        if result > num:
            result = num
    return result




result = find_min_max([3, 1, 7, 2, 5])
result_2 = find_min_max_2([3, 1, 7, 2, 5])
result_3 = find_min([3, 1, 7, 2, 5])
result_4 = find_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
print(result_2)  # (1, 7)
print(result_3)  
print(result_4)  
