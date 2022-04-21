import pytest
import hello_world as logic


@pytest.mark.parametrize(
    'a, b, expected', [(1, 2, 3), (5, 5, 10), (3, 'foo', TypeError())]
)
def test_function_1(a, b, expected):
    if isinstance(expected, Exception):
        with pytest.raises(type(expected)):
            logic.function_1(a, b)
    else:
        assert logic.function_1(a, b) == expected
