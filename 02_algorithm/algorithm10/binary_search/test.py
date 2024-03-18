arr = [12,4,5,1,32,3,45,61,40]
arr.sort()

def binarySearch(target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

print(binarySearch(12))