# 아래 함수를 수정하시오.
def capitalize_words(s):
    new = s.title()
    return new

def capitalize_words_2(s):
    result = ''
   
    for index in range(len(s)):

        if index == 0 or temp == ' ':
            result += s[index].upper()
        else:
            result += s[index]
        temp = s[index]
    return result

result = capitalize_words("hello, world!")
result_2 = capitalize_words_2("hello, world!")
print(result)
print(result_2)
