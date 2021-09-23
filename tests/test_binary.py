import pytest

from radix import Bin, Num
from radix.binary import CACHE


def test_2s_compl():

    n1 = Bin(-13)

    assert '-13' in CACHE
    assert n1.twos_compl() == '10011'

    n2 = Bin(19)

    assert '19' in CACHE
    assert n2.twos_compl() == '010011'

    n3 = Bin(-10.75)
    assert n3.twos_compl() == '10101.01'


def test_1s_compl():

    n1 = Bin(-25)
    assert n1.ones_compl() == '100110'

    n2 = Bin(42)
    assert n2.ones_compl() == '0101010'

    n3 = Bin(-10.75)
    assert n3.ones_compl() == '10101.00'


def test_sign_mag():

    n1 = Bin(-25)
    assert n1.sign_mag() == '111001'

    n2 = Bin(42)
    assert n2.sign_mag() == '0101010'

    n3 = Bin(-10.75)
    assert n3.sign_mag() == '11010.11'


def test_formatting():

    n1 = Bin(-13)
    res = n1.format()

    assert res == '11110011'

    n2 = Bin(-19)
    res = n2.format(size=16, blanks_every=4)

    assert res == '1111 1111 1110 1101'


def test_complement_add():

    n = Bin(-7) + Bin(2)

    assert str(n) == '1011'
    assert type(n).__name__ == 'Bin'
    with pytest.raises(NotImplementedError):
        n.value


def test_complement_subtract():

    n = Bin(-7) - Bin(2)

    assert str(n) == '10111'
    assert type(n).__name__ == 'Bin'
    with pytest.raises(NotImplementedError):
        n.value


def test_complement_multiple_ops():

    with pytest.raises(NotImplementedError):
        (Bin(5) - Bin(-2)) * Bin(-3) + Bin(10)

    n = (Num(5) - Num(-2)) * Num(-3) + Num(10)
    res = Bin.from_Num(n)

    assert str(res) == '10101'
