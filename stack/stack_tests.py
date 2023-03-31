from stack import *
import pytest


@pytest.mark.parametrize('range_limit, pop_limit, expected_result', [
    (0, 0, []), (0, 1, [None]), (1, 1, [0]), (2, 1, [1]), (100, 1, [99]), (100, 10, [i for i in range(99, 89, -1)])])
def test_push(range_limit, pop_limit, expected_result):
    pop_stack_arr = []
    stack = Stack()
    for i in range(range_limit):
        stack.push(i)

    for i in range(pop_limit):
        pop_stack_arr.append(stack.pop())

    assert pop_stack_arr == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 1), (2, 2), (1000, 1000)])
def test_size_after_push(range_limit, expected_result):
    stack = Stack()
    for i in range(range_limit):
        stack.push(i)

    assert stack.size() == expected_result


@pytest.mark.parametrize('range_limit, pop_limit, expected_result', [
    (0, 0, None), (1, 1, 0), (2, 1, 1), (100, 10, 90), (100, 101, None), (10000, 1000, 9000)
])
def test_pop(range_limit, pop_limit, expected_result):
    stack = Stack()
    for i in range(range_limit):
        stack.push(i)

    for j in range(pop_limit - 1):
        stack.pop()

    assert stack.pop() == expected_result


@pytest.mark.parametrize('range_limit, pop_limit, expected_result', [
    (0, 0, 0), (1, 1, 0), (2, 1, 1), (100, 10, 90), (100, 100, 0)
])
def test_size_after_pop(range_limit, pop_limit, expected_result):
    stack = Stack()
    for i in range(range_limit):
        stack.push(i)

    for j in range(pop_limit):
        stack.pop()

    assert stack.size() == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, None), (1, 0), (2, 1), (100, 99)])
def test_peek(range_limit, expected_result):
    stack = Stack()
    for i in range(range_limit):
        stack.push(i)

    assert stack.peek() == expected_result

