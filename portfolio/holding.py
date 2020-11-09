from portfolio.constants import box_titles

"""
A single holding in a portfolio.  A single holding consists of
a ticker
a fund name
a fund class (US, ID, EM, GL60 for a global fund that is 60% US, and GL65)
values for each morningstar style box, sv, sb, sg, mv, mb, mg, lv, lg, lg
"""


class Holding(dict):

    def __init__(self, a_holding):
        super().__init__()
        for k in a_holding:
            v = a_holding[k].replace("$", "")
            v = v.replace(",", "");
            self[k] = v

    """
    This holding's total value
    """

    def total(self):
        return self.total_filtered(lambda k: True)

    """
    The total value of some boxes of the holding.  The fields that pass the
    predicate function are totaled, others are ignored.
    """

    def total_filtered(self, predicate):
        tot = 0
        for k in box_titles:
            if predicate(k):
                tot += int(self[k])
        return tot
