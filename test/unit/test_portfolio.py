from raw_amounts.holding import Holding
from raw_amounts.portfolio import Portfolio
from test.unit.csv_holdings import hold0, hold1, hold2


def test_total0():
    port = Portfolio()
    h0 = Holding(hold0)
    port.append(h0)
    assert h0.total() == port.total()

def test_totl1():
    port = Portfolio()
    h0 = Holding(hold0)
    h1 = Holding(hold1)
    port.append(h0)
    port.append(h1)
    assert h0.total() + h1.total() == port.total()


def test_totl2():
    port = Portfolio()
    h0 = Holding(hold0)
    h1 = Holding(hold1)
    h2 = Holding(hold2)
    port.append(h0)
    port.append(h1)
    port.append(h2)
    subp = port.sub_port(lambda h : h['ticker'] == 'DFEOX' or h['ticker'] == 'DFEVX')
    assert h0.total() + h1.total() == subp.total()


def test_totl3():
    port = Portfolio()
    h0 = Holding(hold0)
    h1 = Holding(hold1)
    h2 = Holding(hold2)
    port.append(h0)
    port.append(h1)
    port.append(h2)
    assert 18099 == port.total(lambda k : k[1] == 'g')
