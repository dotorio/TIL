import sys
sys.stdin = open('input.txt')

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
            print('Stack is Empty!')
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

for tc in range(1, 11):
    # 각 테스트마다
    N, word = input().split()
    # 문자열 길이와 문자열을 받는다
    stack = Stack(int(N))
    # 문자열 길이만큼의 stack을 만든다
    for char in word:
        if stack.get() == char:
            stack.pop()
            # 문자열을 순회하면서 직전 스택에 쌓인 것과 같다면
            # 스택에서 빼낸다
        else:
            stack.push(char)
            # 그렇지 않다면 스택에 넣는다
    print(stack.top+1)
    print(f'#{tc} {"".join(stack.data[:stack.top+1])}')
    # print(f'#{tc} {stack.data}')

    # 완성된 문자열을 출력한다
