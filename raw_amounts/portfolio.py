"""
A Portfolio is a collection of holdings.
"""


class Portfolio(dict):

    def __init__(self):
        super().__init__()

    """
    Create a new sub-raw_amounts based on a given predicate.  The existing
    raw_amounts is unchanged.
    """

    def sub_port(self, predicate):
        new_port = Portfolio()
        for holding in self:
            if predicate(holding):
                new_port.append(holding)
        return new_port

    def total(self, predicate=lambda p: True):
        tot = 0
        for h in self:
            tot += h.total(predicate)
        return tot
