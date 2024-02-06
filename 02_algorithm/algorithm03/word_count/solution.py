import sys
sys.stdin = open('sample_input.txt')

T = int(input())
# 테스트의 개수를 받는다
for case in range(1, T+1):
    # 각 테스트마다
    word1 = list(input())
    word2 = list(input())
    # 비교할 두 문자열을 받는다
    dict = {}
    # word1의 글자들을 이용할 딕셔너리를 만들고
    max_word = 0
    # 가장 많은 글자수를 0으로 설정한다.
    for i in word1:
        dict[i] = 0
        # word1를 순회하며 안의 글자들을 모두 key로 만들고
    for i in word2:
        if i in word1:
            dict[i] += 1
            # word2를 순회하며 word1의 글자를 발견할 때마다
            # 그 value를 1 더한다

    print(f'#{case} {max(dict.values())}')
    # 케이스와 최댓값을 출력한다.