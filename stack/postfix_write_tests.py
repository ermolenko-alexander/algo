import pytest
from postfix_write import *


@pytest.mark.parametrize('input_exp, expected_result', [
    ('8 2 + 4 - =', 6), ('8 2 / 4 - =', 0),  ('8 2 + 5 * 9 + =', 59), ('2 3 - 3 *', -3), ('1 1 * 2 +', 3)
])
def test_get_result_ok(input_exp, expected_result):
    assert expression(input_exp) == expected_result


@pytest.mark.parametrize('input_exp', [
    '1 2 + v =', '! 69 32 1 * -'
])
def test_get_result_exception(input_exp):
    with pytest.raises(ValueError):
        assert expression(input_exp)
