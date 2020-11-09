import csv
from enum import Enum

from portfolio.holding import Holding

csv_line_format = ''

box_titles = ['sv', 'sb', 'sg', 'mv', 'mb', 'mg','lv', 'lb', 'lg']


def make_a_holding(row):
    return Holding(row)


def read_csv(filename):
    row_type = Enum('row_type', 'init, port, ignore')
    this_row = row_type.init
    port = []
    with open(filename) as fil:
        csv_reader = csv.DictReader(fil)
        for row in csv_reader:
            if row['ticker'] == "#":
                this_row = row_type.ignore
            #print(row)
            if this_row == row_type.init:
                titles = row
                this_row = row_type.port
            elif this_row == row_type.port:
                holding = make_a_holding(row)
                port.append(holding)
    for r in port:
        print(r)



def main():
    fn = "../StockStyleAll20201108.csv"
    port = read_csv(fn)



if __name__ == "__main__":
    main()

