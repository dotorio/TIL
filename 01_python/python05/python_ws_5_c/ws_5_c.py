def restructure_word(word, arr):
    for x in word:
        if x.isdecimal():
            for y in range(int(x)):
                arr.pop()
        else:
            arr.remove(x)

    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []
arr_2 = []
for x in original_word:
    arr_2.append(x)

arr.extend(arr_2)
print(arr)
result = restructure_word(word, arr)
print(result)
print(''.join(result))
