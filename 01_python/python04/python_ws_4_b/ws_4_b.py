food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
for x in food_list:
    if x['이름'] == '토마토':
        x['종류'] = '과일'
    
    if x['이름'] == '자장면':
        print(f'{x["이름"]}엔 고춧가루지')
    print(f'{x["이름"]} 은/는 {x["종류"]} (이)다.')
print(food_list)

food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

x=0
while x != len(food_list):
    if food_list[x]['이름'] == '토마토':
        food_list[x]['종류'] = '과일'
    
    if food_list[x]['이름'] == '자장면':
        print(f'{food_list[x]["이름"]}엔 고춧가루지')
    print(f'{food_list[x]["이름"]} 은/는 {food_list[x]["종류"]} (이)다.')
    x+=1
print(food_list)    