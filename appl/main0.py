from appl.utils import csv_to_port, port_to_str, port_to_csv


def main():
    fn = "../StockStyleAll20201111.csv"
    port = csv_to_port(fn)
    disp_a_port(port)
    port_to_csv(port, "Total, $" + str(port.total()), '../total.csv')
    tot_port = port.total()

    us = port.sub_port(lambda r: r['class'] == 'US')
    us_tot = us.total()
    us_percent = us_tot / tot_port
    print('\nUS')
    disp_a_port(us)
    port_to_csv(us, "US,$" + str(us_tot) + ",pc of total:," + str(us_percent), '../us.csv')

    id = port.sub_port(lambda r: r['class'] == 'ID')
    id_tot = id.total()
    id_percent = id_tot / tot_port
    print('\nID')
    disp_a_port(id)
    port_to_csv(id, "Int'l Dev,$" + str(id_tot) + ",pc of total:," + str(id_percent), '../id.csv')

    em = port.sub_port(lambda r: r['class'] == 'EM')
    em_tot = em.total()
    em_percent = em_tot / tot_port
    print('\nEM')
    disp_a_port(em)
    port_to_csv(em, "EM,$" + str(em_tot) + ",pc of total:," + str(em_percent), '../em.csv')


def disp_a_port(port):
    str_form = port_to_str(port)
    print(str_form)


if __name__ == "__main__":
    main()
