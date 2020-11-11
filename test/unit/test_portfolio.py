from math import isclose

import pytest

from raw_amounts.holding import Holding
from raw_amounts.portfolio import Portfolio
from test.unit.csv_holdings import hold0, hold1, hold2


def test_total0():
    port = Portfolio()
    h0 = Holding(hold0)
    port.append(h0)
    assert h0.total() == port.total()


def test_total1():
    port = Portfolio()
    h0 = Holding(hold0)
    h1 = Holding(hold1)
    port.append(h0)
    port.append(h1)
    assert h0.total() + h1.total() == port.total()


def test_total2():
    port = Portfolio()
    h0 = Holding(hold0)
    h1 = Holding(hold1)
    h2 = Holding(hold2)
    port.append(h0)
    port.append(h1)
    port.append(h2)
    subp = port.sub_port(lambda h: h['ticker'] == 'DFEOX' or h['ticker'] == 'DFEVX')
    assert h0.total() + h1.total() == subp.total()


def test_total3():
    port = Portfolio()
    h0 = Holding(hold0)
    h1 = Holding(hold1)
    h2 = Holding(hold2)
    port.append(h0)
    port.append(h1)
    port.append(h2)
    assert 18099 == port.total(lambda k: k[1] == 'g')

def test_total4():
    port = Portfolio()
    h0 = Holding(hold0)
    h1 = Holding(hold1)
    h2 = Holding(hold2)
    port.append(h0)
    port.append(h1)
    port.append(h2)
    # 0.110908286	0.111018918	0.111240181 for mv mb mg
    expect = {'mv': .110908286, 'mb': .111018918, 'mg': .111240181}
    ratio = port.ratio(lambda k: k[0] == 'm')
    assert len(ratio) == 3
    assert pytest.approx(expect['mv']) == ratio['mv']
    assert pytest.approx(expect['mb']) == ratio['mb']
    assert pytest.approx(expect['mg']) == ratio['mg']
