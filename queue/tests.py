from queue import *
import pytest


@pytest.mark.parametrize('start, finish, expected_result', [(0, 5, 0), (100, 111, 100), (1, 2, 1)])
def test_enqueue(start, finish, expected_result):
    q = Queue()
    for i in range(start, finish):
        q.enqueue(i)
    assert q.dequeue() == expected_result


@pytest.mark.parametrize('start, finish, dif, expected_result', [
    (2, 10, 1, 9), (0, 1, 0, None)])
def test_dequeue(start, finish, dif, expected_result):
    q = Queue()
    for i in range(start, finish):
        q.enqueue(i)
    for i in range(start, finish - dif):
        q.dequeue()
    assert q.dequeue() == expected_result


@pytest.mark.parametrize('range_limit, expected_result', [(0, 0), (1, 1), (1000, 1000)])
def test_size(range_limit, expected_result):
    q = Queue()
    for i in range(range_limit):
        q.enqueue(i)
    assert q.size() == expected_result
