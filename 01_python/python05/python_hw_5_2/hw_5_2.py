# 아래 함수를 수정하시오.
def count_character(string, o):
    number_o = 0
    for x in string:
        if x == o:
            number_o += 1
    return number_o

def count_character_2(string, o):
    return string.count(o)

result = count_character("Hello, World!", "o")
result_2 = count_character_2("Hello, World!", "o")

print(result)  # 2
print(result_2)  # 2
