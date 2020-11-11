from raw_amounts.constants import box_titles

"""
A single holding in a raw_amounts.  A single holding consists of
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
     The total value of some boxes of the holding.  The fields that pass the
    predicate function are totaled, others are ignored.
    
    The default totals all of the boxes.
    """

    def total(self, predicate=lambda k: True):
        tot = 0
        for k in box_titles:
            if predicate(k):
                tot += int(self[k])
        return tot
