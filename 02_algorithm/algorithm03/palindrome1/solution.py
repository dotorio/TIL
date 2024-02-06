import sys
sys.stdin = open('input.txt')

for case in range(1, 11):
    # 각 테스트마다
    length = int(input())
    # 찾아야 하는 회문의 길이를 받는다
    arr = [list(map(str, input())) for i in range(8)]
    # 8 * 8 크기의 글자판을 배열로 받는다
    find = 0
    # 찾아낸 회문의 개수를 0으로 설정
    for i in arr:
        # 글자판의 행마다
        for j in range(8-length+1):
            # 글자판의 범위를 벗어나지 않도록 열의 범위를 설정하고
            word = i[j:j+length]
            # 회문의 길이만큼 슬라이싱해서 글자를 얻는다
            if "".join(map(str,word)) == "".join(map(str,word[::-1])):
                find += 1
                # 얻은 글자가 회문이라면 find를 1 올린다
    arr = zip(*arr[::-1])
    # 배열을 90도 회전시켜 세로에서 찾기를 시작한다
    for i in arr:
        for j in range(8-length+1):
            word = i[j:j+length]
            if "".join(map(str,word)) == "".join(map(str,word[::-1])):
                find += 1
                # 아까와 같은 방법으로 회문을 찾는다
    print(f'#{case} {find}')
    # 케이스와 find를 출력한다.


