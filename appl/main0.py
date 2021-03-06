from appl.utils import csv_to_port, port_to_str, port_to_csv

funds = ['DFEOX', 'DFFVX', 'DFISX', 'DFIVX', 'DFEVX', 'DGS', 'VIOV', 'VWILX']

def main():
    # fn = "../StockStyleAll20201111b.csv"
    fn = "../StockStyle20201205.csv"
    # fn = "../StockStyle401k20191105.csv"
    port = csv_to_port(fn)
    print('\nTotal Portfolio ', fn, '\n', "Total, $" + str(port.total()))
    disp_a_port(port)
    port_to_csv(port, "Total, $" + str(port.total()), '../total.csv')
    tot_port = port.total()

    us = port.sub_port(lambda r: r['class'] == 'US')
    us_tot = us.total()
    us_percent = us_tot / tot_port
    print('\nUS\n', "US,$" + str(us_tot) + ",pc of total:," + str(us_percent))
    disp_a_port(us)
    port_to_csv(us, "US,$" + str(us_tot) + ",pc of total:," + str(us_percent), '../us.csv')

    id = port.sub_port(lambda r: r['class'] == 'ID')
    id_tot = id.total()
    id_percent = id_tot / tot_port
    print('\nID\n', "Int'l Dev,$" + str(id_tot) + ",pc of total:," + str(id_percent))
    disp_a_port(id)
    port_to_csv(id, "Int'l Dev,$" + str(id_tot) + ",pc of total:," + str(id_percent), '../id.csv')

    em = port.sub_port(lambda r: r['class'] == 'EM')
    em_tot = em.total()
    em_percent = em_tot / tot_port
    print('\nEM\n', "EM,$" + str(em_tot) + ",pc of total:," + str(em_percent))
    disp_a_port(em)
    port_to_csv(em, "EM,$" + str(em_tot) + ",pc of total:," + str(em_percent), '../em.csv')

    gl = port.sub_port(lambda r: r['class'] == 'GL')
    gl_tot = gl.total()
    gl_percent = gl_tot / tot_port
    print('\nGL\n', "GL,$" + str(gl_tot) + ",pc of total:," + str(gl_percent))
    disp_a_port(gl)
    port_to_csv(em, "GL,$" + str(gl_tot) + ",pc of total:," + str(gl_percent), '../gl.csv')

    for t in funds:
        sf = port.sub_port(lambda r: r['ticker'] == t)
        sf_tot = sf.total()
        sf_percent = sf_tot / tot_port
        print('\n\n', t, '\n', "$", str(sf_tot) + ",  pc of total:," + str(sf_percent))
        disp_a_port(sf)



def disp_a_port(port):
    str_form = port_to_str(port)
    print(str_form)


if __name__ == "__main__":
    main()
