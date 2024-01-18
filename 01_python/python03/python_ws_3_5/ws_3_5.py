number_of_people = 0
number_of_book = 100


def increase_user():
    pass


names = ['김시습', '허균', '남영로', '임제', '박지원']
ages = [20, 16, 52, 36, 60]
addresses = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    print(f'{name}님 환영합니다!')
    user = {'name': name, 'age': age, 'address': address}
    return user

def decrease_book(number):
    global number_of_book
    remain_book = number_of_book - number
    print(f'남은 책의 수 : {remain_book}')

def make_dict(list):
    for a in list:
        name




many_user = list(map(create_user, names, ages, addresses))
print(many_user)
info = dict(map(, many_user))


def rental_book(info):

    pass
