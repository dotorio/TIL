def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0] # 퀵 소트의 pivot 위치는 아무 대상이어도 상관없다.
        # 피벗보다 작은 대상만 모음
        less_than_pivot = [x for x in lst[1:] if x <= pivot]
        # 피벗보다 큰 대상만 모음
        greater_than_pivot = [x for x in lst[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

arr = [3, 6, 8, 10, 1, 2, 1]
N = len(arr)
result = quick_sort(arr)
print(result)