from stack import *


def check(brackets):
    stack = Stack()
    for bracket_str in brackets:
        if bracket_str == '(':
            stack.push('(')
        elif bracket_str == ')' and stack.peek() == '(':
            stack.pop()
        elif bracket_str == ')' and stack.size() == 0:
            return False

    return stack.size() == 0
