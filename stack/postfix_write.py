from stack import *


def get_elements(stack2):
    a = stack2.pop()
    b = stack2.pop()
    return a, b

def expression(input_str):
    stack1 = Stack()
    stack2 = Stack()
    for i in input_str.strip().split()[::-1]:
        stack1.push(i)

    for _ in range(stack1.size()):
        curr = stack1.pop()
        if curr.isdigit():
            stack2.push(int(curr))
        elif curr == '+':
            a, b = get_elements(stack2)
            stack2.push(a + b)
        elif curr == '-':
            a, b = get_elements(stack2)
            stack2.push(-a + b)
        elif curr == '*':
            a, b = get_elements(stack2)
            stack2.push(a * b)
        elif curr == '=':
            stack2.push(stack2.pop())
        else:
            raise ValueError('Error in value')

    if stack2.size() == 1:
        return stack2.pop()
    else:
        raise ValueError('Error in notation')
