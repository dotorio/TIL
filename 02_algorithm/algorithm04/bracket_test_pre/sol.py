import sys
sys.stdin = open('sample_input.txt')

T = int(input())

class Stack:
    
    # stack을 생성할 때 필요한 값이 있는데,
    # stack의 크기를 지정해야 한다.
    def __init__(self, size):
        
        self.size = size
        # 자료구조 stack을 list를 활용해서 구현
        self.data = [None] * size # 값이 없음을 나타내는 None
        self.top = -1 # 초기 값이 없으므로, top의 위치는 -1

    def push(self, item): # stack에 값 삽입 -> 삽입할 대상 item을 인자로 받는다.
        
        if self.is_full():
            print('Stack is Full!')
        else:
        # 받아온 item을 내 data에 top 번째 위치에 삽입한다.
            self.top += 1 # top위치 1 증가
            self.data[self.top] = item
    
    def get(self): # top번째 있는 요소를 출력할 수 있는 방법
        return self.data[self.top]
    
    def __str__(self): # instance print했을 때, stack안의 data를 바로 출력
        return f'{self.data}'
    
    def pop(self):
        if self.is_empty():
            global result
            result = False
            raise IndexError
        else:
        # top_value = self.data[self.top] = None
        # self.data[self.top] = None
            self.top -= 1
        # return top_value
            return self.data[self.top + 1]
    
    def is_empty(self):
        # top이 -1을 가리키고 있다면 stack은 비었다.
        return self.top == -1
    
    def is_full(self):
        return self.size == self.top + 1    

for tc in range(1, T+1):
    # 각 테스트마다
    code = input()
    # 문자열을 받는다
    stack = Stack(100)
    # 크기 100짜리 stack을 만든다
    result = True
    # result의 기본값은 True
    cnt = 0
    # 스택에 쌓인 개수를 설정
    for i in range(len(code)):
        if code[i] == '(':
            stack.push(')')
            cnt += 1
        if code[i] == '{':
            stack.push('}')
            cnt += 1
            # 각 글자가 (, { 라면 스택에 ), }로 쌓고 쌓인 개수를 1 올린다
        if code[i] == ')' or  code[i] == '}':
            if code[i] == stack.get():
                stack.pop()
                cnt -= 1
                # 각 글자가 ), } 라면 바로 직전 스택에 쌓인 것과 비교해서
                # 같다면 스택에서 빼내고 쌓인 개수를 1 내린다
            else:
                result = False
                break
            # 만약 직전 스택에 쌓인 것과 같지 않다면
            # result를 False로 바꾼다
    if cnt != 0:
        result = False
        # 문자열을 모두 순회했는데
        # 만약 스택에 쌓인 개수가 0이 아니라면
        # result를 False로 바꾼다
    if result == False:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
        # result에 따라서 맞는 결과를 출력한다.





