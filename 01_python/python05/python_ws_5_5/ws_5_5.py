# 아래 함수를 수정하시오.
def even_elements(my_list):
    a = []
    b = []
    for x in my_list:
        if x % 2 == 1:
            my_list.remove(x)
    while my_list != []:
        item = my_list.pop(0)
        a.append(item)
    b.extend(a)
    return b
    
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
