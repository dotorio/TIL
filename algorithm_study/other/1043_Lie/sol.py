import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

# 진실을 아는 사람 번호들을 리스트로 묶는다
know_cnt, *know_mem = map(int, input().split())

# 파티들의 정보를 넣을 딕셔너리
parties = dict()

# 어느 멤버가 무슨 파티에 가는지 정보를 넣을 딕셔너리
mem_to_party = dict()
for i in range(1, N+1):
    mem_to_party[i] = []

# 파티들을 받으면서 두 딕셔너리에 정보를 채운다
for par in range(M):
    par_cnt, *party = map(int, input().split())
    parties[i] = party
    for mem in party:
        mem_to_party[mem].append(i)

# 이 멤버에게 구라쳐도 되는가? True 안되나? False
member = [True]*(N+1)

# 이 파티에서 구라쳐도 되는가? True 안되나? False
can_lie_party = [True]*M

# 진실을 아는 멤버들을 순회하면서
for now_mem in know_mem:

    # 이 멤버에게 구라치면 안되므로 False로 변경
    member[now_mem] = False

    # 이 멤버가 속한 파티 번호를 순회하며
    for par in mem_to_party[now_mem]:

        # 이 파티에서 구라치면 안되므로 False로 변경
        can_lie_party[par] = False

        # 구라치면 안되는 파티에 속한 사람들은
        # 진실을 들었기 때문에 진실을 아는 멤버가 된다
        for mem in parties[par]:

            # 이미 속한 멤버가 아니라면 리스트에 넣기
            if mem not in know_mem:
                know_mem.append(mem)

# 구라쳐도 되는 파티의 개수를 출력
print(can_lie_party.count(True))