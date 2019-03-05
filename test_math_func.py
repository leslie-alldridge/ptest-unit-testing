import math_func
import pytest
import sys


@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9


@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10


@pytest.mark.strings
def test_add_string():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result


@pytest.mark.skipif(sys.version_info > (3.3), reason="Don't run if python is too new")
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result


@pytest.mark.parametrize('num1, num2, result', [
    (7, 3, 10),
    ('Hello', ' World', 'Hello World')
])
def test_add2(num1, num2, result):
    assert math_func.add(num1, num2) == result
