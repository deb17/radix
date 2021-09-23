from radix import dim_radix_compl, radix_compl, Num


def test_9s_complement():

    num1 = Num(546700)
    nines_compl = dim_radix_compl(num1)

    assert nines_compl == '453299'

    num2 = Num('012398')
    nines_compl = dim_radix_compl(num2)

    assert nines_compl == '987601'


def test_10s_complement():

    num1 = Num('012398')
    tens_compl = radix_compl(num1)

    assert tens_compl == '987602'

    num2 = Num(246700)
    tens_compl = radix_compl(num2)

    assert tens_compl == '753300'
