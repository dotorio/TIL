string = list(input())
explode = list(input())

# 문자를 넣을 stack, 폭발을 위한 인덱스를 저장할 idx_Stack
stack, idx_stack = [], []
len_ex, len_str = len(explode), len(string)
str_idx, ex_idx = 0, 0

# string을 다 순회할 때까지 반복
while str_idx != len_str:

    # 일단 stack에 현재 위치 string 문자를 넣음
    stack.append(string[str_idx])

    # 방금 넣은 문자가 폭발 문자열의 위치와 같다면
    if string[str_idx] == explode[ex_idx]:

        # 두 인덱스 모두 1 더함
        str_idx += 1
        ex_idx += 1

        # 만약 폭발 문자열의 마지막까지 넣어서 지울 차례이면
        if ex_idx == len_ex:

            # 지울 위치를 지움
            del stack[-len_ex:]

            # 다음에 불러올 인덱스가 없다면 0으로
            if not idx_stack:
                ex_idx = 0

            # 불러올 인덱스가 있다면 pop해서 들고옴
            else:
                ex_idx = idx_stack.pop()
    
    # 방금 넣은 문자가 폭발 문자열의 위치와 다르다면
    else:

        # string 인덱스만 1 더하고
        str_idx += 1

        # 만약 폭발 문자열의 일부가 더해지는 중이었으면
        if ex_idx:

            # 인덱스 스택에 넣어서 저장해둠
            idx_stack.append(ex_idx)

            # 폭발 인덱스 초기화
            ex_idx = 0

            # 방금 스택에 더한거 빼고
            stack.pop()

            # string 인덱스 1 뺌
            str_idx -= 1

        # 만약 폭발 문자열의 일부가 더해지는 중이 아니었으면
        else:

            # 인덱스 스택에 0 넣음
            idx_stack.append(0)

# 출력할 문자가 남아있다면 출력
if stack:
    print(''.join(stack))

# 없으면 FRULA 출력
else:
    print('FRULA')