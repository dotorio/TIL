import sys
sys.stdin = open("input.txt")

def quick_sort(arr):
    # 쪼갠 배열의 길이기 1 이하라면 그대로 리턴
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    # 피벗보다 작으면 왼쪽에, 크면 오른쪽에 넣는다
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    # left, 피벗, right를 합친다
    return quick_sort(left) + [pivot] + quick_sort(right)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(arr)[N//2]}')