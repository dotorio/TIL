import sys
sys.stdin = open('input.txt')

# 테스트의 개수를 받는다
T = int(input())

# 함수의 정의는 함수 호출 시에 올라와서 본다
def delete(word):
    # 문자열 길이 - 1의 범위에서
    for i in range(len(word)-1):
        # i번째와 i+1번째 문자가 같다면
        if word[i] == word[i+1]:
            # 그 두 문자를 없앤다
            word.pop(i)
            word.pop(i)
            # 새로운 문자열을 변수로 함수 호출
            return delete(word)
    # 한번도 같은 경우가 없었다면
    else:
        # 그 문자열을 리턴
        return word

# 각 테스트마다
for tc in range(1, T+1):
    # 문자열을 받는다
    string = list(input())
    # 문자열을 변수로 함수를 호출한다
    delete(string)
    # 완성된 문자열의 길이를 출력한다
    print(f'#{tc} {len(string)}')