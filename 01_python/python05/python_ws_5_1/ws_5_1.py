# 아래 함수를 수정하시오.
def reverse_string(x):
    my_list = list(x)
    my_list.reverse()
    return ''.join(my_list)

def reverse_string_2(x):

    return x[::-1]

def reverse_string_3(x):

    return ''.join(reversed(x))

def reverse_string_4(x):
    result = ''
    for index in range(len(x)-1, -1, -1):
        result += x[index]
    return result
    
                       
    



result = reverse_string("Hello, World!")
result_2 = reverse_string_2("Hello, World!")
result_3 = reverse_string_3("Hello, World!")
result_4 = reverse_string_4("Hello, World!")
print(result)  # !dlroW ,olleH
print(result_2)  # !dlroW ,olleH
print(result_3)  # !dlroW ,olleH
print(result_4)  # !dlroW ,olleH
