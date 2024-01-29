import sys
sys.stdin = open('input.txt')

for _ in range(10):
    dump = int(input())
    box_list = list(map(int, input().split()))
    for i in range(dump):
        the_max = box_list.index(max(box_list))
        the_min = box_list.index(min(box_list))
        box_list[the_max] -= 1
        box_list[the_min] += 1

    result = max(box_list) - min(box_list)
    print(f'#{_+1} {result}')