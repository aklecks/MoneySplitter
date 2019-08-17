from help_functions import *
from quickmaffs2 import *
from argparse import ArgumentParser

# TODO Einlesen von excel Tabelle
# TODO Ausgabe von Summen der Ausgaben der Teilnehmer jeweils + Differenz zum Durchschnitt (vermutlich am einfachsten als pandas Tabelle)
# TODO clean Code
# TODO option für Spalte mit Verwendungszwecken


if __name__ == '__main__':

    # some command line options
    parser = ArgumentParser()
    parser.add_argument('--file', dest='filepath', default=None)
    parser.add_argument('--create_data', dest='create_data_flag', default=False)
    args = parser.parse_args()

    filepath = args.filepath
    create_data_flag = args.create_data_flag
    filepath = 'data/bigdata.csv'

    if filepath is None:
        filepath = input('Bitte Pfad zur csv Tabelle eingeben: \n')

    if create_data_flag:
        create_data(3000, 500, use_real_names=False)
        filepath = 'data/bigdata.csv'

    # filepath = 'data/open_office_test.csv'
    # filepath = 'data/bigdata.csv'

    # load the data
    data = load_data(filepath)

    # calculate
    quickmaffs2(data)
