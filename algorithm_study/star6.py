number = int(input())
for i in range(number):
    star_count = (number - i) * 2 - 1 
    blank_count = i
    print(' ' * blank_count, end = '')
    print('*' * star_count, end = '')
    if i != number - 1:
        print(' ')