class Holding (dict):

    def __init__(self, a_holding):
        super().__init__()
        for k in a_holding:
            v = a_holding[k].replace("$", "")
            v = v.replace(",", "");
            self[k] = v


