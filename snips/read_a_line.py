import csv

def read_one_line(filename):
    with open(filename) as fil:
        csv_reader = csv.reader(fil)
        for row in csv_reader:
            print(row)


def main():
    fn = "../StockStyleAll20201108.csv"
    read_one_line(fn)


if __name__ == "__main__":
    main()
