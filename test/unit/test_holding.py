from security_coll.holding import Holding
from test.unit.csv_holdings import hold0, hold1, hold2


def test_total0():
    holding = Holding(hold0)

    assert 9078 == holding.total()


def test_total1():
    holding = Holding(hold1)
    assert 2007 == holding.total(lambda k: k == 'mb')


def test_total2():
    holding = Holding(hold2)
    assert 9049 == holding.total(lambda k: k[0] == 'l')


def test_total3():
    holding = Holding(hold0)
    assert 3033 == holding.total(lambda k: k[1] == 'g')
