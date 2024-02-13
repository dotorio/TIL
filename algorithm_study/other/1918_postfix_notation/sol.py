isp = {'(':0, '+':1, '-':1, '*':2, '/':2, ')':-1}
icp = {'(':3, '+':1, '-':1, '*':2, '/':2, ')':-1}
stack = []

formula = input()
for i in formula:
    if i not in isp:
        print(i, end = '')
    else:
        if stack == []:
            stack.append(i)
        elif i == ')':
            now = stack.pop()
            while now != '(':
                print(now, end='')
                now = stack.pop()
        else:
            if isp[stack[-1]] < icp[i]:
                stack.append(i)
            else:
                while stack != [] and isp[stack[-1]] >= icp[i]:
                    print(stack.pop(), end='')
                stack.append(i)
while stack:
    print(stack.pop(), end='')


        