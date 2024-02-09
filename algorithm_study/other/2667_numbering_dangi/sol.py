import sys
sys.stdin = open('input.txt')

# 지도의 크기를 받는다
N = int(input())
# 지도를 입력으로 받는다
map = list(list(map(int, input())) for _ in range(N))
# 방문을 표시할 지도2를 만든다
map2 = list([False] * N for _ in range(N))
# 인접한 1과의 연결을 표시할 딕셔너리를 만든다
con = {}
# 각 좌표를 key로 하는 리스트를 딕셔너리 안에 넣는다
for j in range(N):
    for i in range(N):
        con[(j, i)] = []
# 지도를 순회하며 인접한 1과의 연결을 딕셔너리 안에 넣는다
for j in range(N):
    for i in range(N):
        if map[j][i] == 1:
            if i-1 >= 0 and map[j][i-1] == 1:
                con[(j, i)].append([j, i-1])
            if j-1 >= 0 and map[j-1][i] == 1:
                con[(j, i)].append([j-1, i])
            if i+1 <= N-1 and map[j][i+1] == 1:
                con[(j, i)].append([j, i+1])
            if j+1 <= N-1 and map[j+1][i] == 1:
                con[(j, i)].append([j+1, i])
# 단지의 개수를 0으로 설정
dangi_cnt = 0
# 단지내 집 수를 리스트로 만든다
cnt = []
for j in range(N):
    for i in range(N):
        # 지도를 순회하며 1이며 방문하지 않은 곳이라면
        if map[j][i] == 1 and map2[j][i] == False:
            # 스택을 만들고 인접한 연결 리스트를 스택에 넣는다
            stack = []
            stack.extend(con[(j, i)])
            # 단지내 집 수를 1로 설정
            this_dangi = 1
            # 방문했으므로 True로 변경
            map2[j][i] = True
            # 스택에 좌표가 없어질 때까지
            while stack:
                # 저장된 마지막 좌표를 꺼내서
                now = stack.pop()
                # 방문하지 않은 곳이라면
                if map2[now[0]][now[1]] == False:
                    # True로 변경
                    map2[now[0]][now[1]] = True
                    # 인접한 연결 리스트를 스택에 넣는다
                    stack.extend(con[(now[0], now[1])])
                    # 단지내 집 수를 1 더함
                    this_dangi += 1
            # 단지 하나가 끝났으므로 단지 개수를 1 더함
            dangi_cnt += 1
            # 단지내 집수를 리스트에 넣는다
            cnt.append(this_dangi)
# 단지 개수를 출력
print(dangi_cnt)
# 단지내 집수를 차례로 출력
cnt.sort()
for i in cnt:
    print(i)