N = int(input())

member = []
for _ in range(N):
    member.append(int(input()))

# 국회위원들의 명예 점수를 오름차순 정렬
member.sort()

# 명예 기준 점수는 1, 해커 숫자는 0 으로 시작
honor, hacker = 1, 0

# 국회위원을 순회하면서
for i in range(N):

    # 첫번째 국회위원이 아니라면
    if i != 0:

        # 이전 점수와 지금 점수를 비교해서 같지 않으면
        if member[i] != member[i-1]:

            # 명예 기준 점수를 1 올리고
            honor += 1

            # 해커 숫자를 (해당 점수 - 명예 기준 점수)만큼 올린다 
            hacker += member[i] - honor

            # 해당 점수는 명예 기준 점수로 바꾼다
            member[i] = honor
        
        # 이전 점수와 지금 점수가 같으면 다음 점수 순회
        else:
            continue
    
    # 첫번째 국회위원이라면
    else:

        # 해커 숫자를 (해당 점수 - 명예 기준 점수)만큼 올린다
        hacker += member[i] - honor

        # 해당 점수는 명예 기준 점수로 바꾼다
        member[i] = honor

# 완성된 해커 숫자를 출력
print(hacker)