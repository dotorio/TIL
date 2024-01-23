# 아래 함수를 수정하시오.
def get_value_from_dict(my_dict, key):
    return my_dict[key], my_dict.get(key)


my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice
