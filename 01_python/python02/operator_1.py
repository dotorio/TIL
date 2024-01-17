one = 3
two = 5
if one or two:
    print('or 연산 통과')
else:
    print('or 연산 통과 못함')

print(0 == False)
print(1 == False)
print(-1 == False)
print('' == False)
print('' == True)

if '':
    print('빈문자열은 if문에서 True?')
else:
    print('빈문자열은 if문에서 False')

if one > 0 or one < 0:
    pass
if one != 0:
    pass

