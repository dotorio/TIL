def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    user = {'name': name, 'age': age, 'address': address}
    return user

names = ['김시습', '허균', '남영로', '임제', '박지원']
ages = [20, 16, 52, 36, 60]
addresses = ['서울', '강릉', '조선', '나주', '한성부']

user_info = list(map(create_user, names, ages, addresses))

print(user_info)