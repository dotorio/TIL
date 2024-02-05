N = int(input())
words = []
sort_words = []
max_len_word = 0
for _ in range(N):
    word = input()
    if max_len_word < len(word):
        max_len_word = len(word)
    words.append(word)
for i in range(1, max_len_word+1):
    list = []
    for a in words:
        if len(a) == i:
            if a not in list:
                list.append(a)
    list.sort()
    sort_words.extend(list)
for i in sort_words:
    print(i)
