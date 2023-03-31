from bracket_balance import *
import pytest


@pytest.mark.parametrize('string, expected_result', [
    ('((())))))', False), (')(((()()()()(', False), ('((())))(())))', False), ('()()()()()', True),
    ('()()()()', True), (')((()', False), ('()))((()', False), ('(()())(())', True),
    ('(kjlasf) wqerwer(6768)', True), ('()', True), (')(', False), ('()))((', False)
])
def test_check_balance(string, expected_result):
    assert check(string) == expected_result