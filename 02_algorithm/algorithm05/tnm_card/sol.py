import sys
sys.stdin = open('input.txt')

def game(members):
    global winner
    # 사람이 하나라면 바로 이긴다
    if len(members) == 1:
        winner.append(members[0])
    # 사람이 둘이면 가위바위보를 한다
    elif len(members) == 2:
        if members[0][1] == members[1][1]:
            winner.append(members[0])
        elif members[0][1] == 1:
            if members[1][1] == 2:
                winner.append(members[1])
            else:
                winner.append(members[0])
        elif members[0][1] == 2:
            if members[1][1] == 1:
                winner.append(members[0])
            else:
                winner.append(members[1])
        else:
            if members[1][1] == 1:
                winner.append(members[1])
            else:
                winner.append(members[0])
    # 사람이 셋 이상이면 문제의 조건에 따라 그룹을 둘로 쪼갠다
    else:
        game(members[:(1+len(members))//2])
        game(members[(1+len(members))//2:])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    # 사람의 번호를 저장할 리스트를 만든다
    members = []
    for i in range(len(cards)):
        members.append([i+1, cards[i]])
    # 사람이 하나 남을 때까지 게임을 반복한다
    while len(members) != 1:
        winner = []
        game(members)
        members = winner
    # 하나 남은 사람의 번호를 출력한다
    print(f'#{tc} {members[0][0]}')