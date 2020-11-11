import csv
from enum import Enum

from raw_amounts.constants import box_titles
from raw_amounts.holding import Holding
from raw_amounts.portfolio import Portfolio

csv_line_format = ''


def make_a_holding(row):
    return Holding(row)


def read_csv(filename):
    row_type = Enum('row_type', 'port, ignore')
    this_row = row_type.port
    port = Portfolio()
    with open(filename) as fil:
        csv_reader = csv.DictReader(fil)
        titles = csv_reader.fieldnames
        # print(titles)
        for row in csv_reader:
            if row['ticker'] == "#":
                this_row = row_type.ignore
                #print(row)
            elif this_row == row_type.port:
                holding = make_a_holding(row)
                port.append(holding)
    for r in port:
        print('contains: ', r.total(), ": ", r)

    for box in box_titles:
        print(box, ": ", port.ratio(lambda b: b==box))
    print(port.ratio())



def main():
    fn = "../StockStyleAll20201108.csv"
    port = read_csv(fn)



if __name__ == "__main__":
    main()

