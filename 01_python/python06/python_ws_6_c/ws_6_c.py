data = [
    {
        'name': 'galaxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galaxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galaxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

for item in data:
    for key in key_list:
        if item.get(key) == None:
            item.setdefault(key, 'unknown')
            print(f'{key}은/는 {item[key]}입니다.')
        else:
            print(f'{key}은/는 {item[key]}입니다.')
    print()
