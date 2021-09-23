import pytest

from radix import Num


def test_base10():

    a_10 = Num(255)
    a_16 = a_10.to(16)

    assert str(a_16) == 'FF'


def test_base16():

    a_16 = Num(20, 16)
    a_2 = a_16.to(2)
    a_10 = a_16.to(10)

    assert str(a_2) == '100000'
    assert str(a_10) == '32'


def test_invalid_num():

    with pytest.raises(ValueError):
        Num('0x20', 16)

    with pytest.raises(ValueError):
        Num('1g', 16)


def test_invalid_base():

    with pytest.raises(ValueError):
        Num('12', 37)


def test_floats():

    a = Num(10.75)
    b = a.to(16)

    assert str(b) == 'A.C'

    c = Num('.c48', 16)
    d = c.to(2)

    assert str(d) == '0.110001001'


def test_unary_op():

    num = -Num('fe', 16).to(2)
    assert str(num) == '-11111110'
    assert num.base == 2


def test_expr():

    res = Num(29).to(8) - Num(10, 8) * Num(2, 8)

    assert res.value == '15'
    assert res.base == 8
