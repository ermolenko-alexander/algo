from stack import *


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
            stack2.push(stack2.pop() + stack2.pop())
        elif curr == '-':
            stack2.push(stack2.pop() - stack2.pop())
        elif curr == '*':
            stack2.push(stack2.pop() * stack2.pop())
        elif curr == '=':
            stack2.push(stack2.pop())
        else:
            raise ValueError('Error in value')

    if stack2.size() == 1:
        return stack2.pop()
    else:
        raise ValueError('Error in notation')
