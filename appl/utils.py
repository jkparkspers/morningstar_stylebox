import csv
from enum import Enum

from raw_amounts.constants import all_titles, box_titles, ms_box_order
from security_coll.holding import Holding
from security_coll.portfolio import Portfolio

"""
Read a csv file and return its portfolio
"""
def csv_to_port(filename):
    # ignore the first row, and all rows after the # appears
    row_type = Enum('row_type', 'init, port, ignore')
    this_row = row_type.init
    port = Portfolio()
    with open(filename) as fil:
        csv_reader = csv.DictReader(fil, all_titles)
        titles = csv_reader.fieldnames
        # print(titles)
        for row in csv_reader:
            if this_row == row_type.init:
                this_row = row_type.port
            elif row['ticker'] == "#":
                this_row = row_type.ignore
                # print(row)
            elif this_row == row_type.port:
                holding = Holding(row)
                port.append(holding)
    return port


"""
Convert the given portfolio into a morningstar style box string
"""
def port_to_str(port):
    ret_str = ''
    ratios = port.ratio()
    for box in ms_box_order:
        if box == '\n':
            ret_str += '\n'
        else:
            ret_str += str(ratios[box]) + ','
    ret_str += '\n'
    return ret_str


def port_to_csv(port, title, filename):
    with open(filename, 'w') as fn:
        fn.write(title + '\n')
        fn.write(port_to_str(port))
        fn.write('\n')
