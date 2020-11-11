"""
A Portfolio is a collection of holdings.
"""
from raw_amounts.constants import box_titles


class Portfolio(list):

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

    """
    Run through all holdings and total them according to the predicate
    """

    def total(self, predicate=lambda p: True):
        tot = 0
        for h in self:
            tot += h.total(predicate)
        return tot

    """
    Figure out the ratio of the portfolio total the selected boxes represent and return it as a dictionary
    """

    def ratio(self, predicate=lambda b: True):
        ratios_dict = {}
        port_tot = self.total()
        for b in box_titles:
            if predicate(b):
                one_box = self.total(lambda p: p == b)
                if port_tot > 0:
                    ratios_dict[b] = one_box / port_tot
                else:
                    ratios_dict[b] = 0
        return ratios_dict
