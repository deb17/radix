import pytest

from radix import expr


def test_valid_expr():

    res = expr('10 + 4 * 4', 5)

    assert res.value == '41'
    assert res.base == 5
    assert type(res).__name__ == 'Num'


def test_invalid_exprs():

    with pytest.raises(ValueError) as excinfo:
        _ = expr('10 + 4 * 5', 5)

    msg = excinfo.value.args[0]
    assert msg == '5 is an invalid base 5 number.'

    with pytest.raises(SyntaxError):
        _ = expr('5 @ 6', 16)


def test_show_input_expr(capsys):

    _ = expr('2.5 * 2.5', show=True)

    out, err = capsys.readouterr()

    assert out == 'Num(\'2.5\', 10)*Num(\'2.5\', 10)\n'
    assert err == ''
