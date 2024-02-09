import sys
sys.stdin = open('input.txt')


while True:
    word = input()
    stack = []
    result = 'yes'
    if word == '.':
        break
    for i in word:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack == [] or stack.pop() != '(':
                result = 'no'
                break            
        elif i == ']':
            if stack == [] or stack.pop() != '[':
                result = 'no'
                break
    if stack != []:
        result = 'no'
    print(result)