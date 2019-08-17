import os
from help_functions import load_data, create_data
from quickmaffs import quickmaffs
from quickmaffs2 import quickmaffs2
from argparse import ArgumentParser

# TODO Ausgabe von Summen der Ausgaben der Teilnehmer jeweils + Differenz zum Durchschnitt (vermutlich am einfachsten als pandas Tabelle)


if __name__ == '__main__':

    # some command line options
    parser = ArgumentParser()
    parser.add_argument('--file', dest='filepath', default=None)
    parser.add_argument('--create_data', dest='create_data_flag', default=False)
    args = parser.parse_args()

    filepath = args.filepath
    create_data_flag = args.create_data_flag

    # stuff for running in IDE
    # filepath = 'data/open_office_test.csv'
    # filepath = 'data/bigdata.csv'
    # create_data_flag = False

    if filepath is None:
        filepath = input('Please enter path to csv file: \n')

    if create_data_flag:
        create_data(300, 500, use_real_names=False)
        filepath = 'data/bigdata.csv'

    # check if filepath is valid
    if not os.path.isfile(filepath):
        # tell them and get correct path
        filepath = input('Sorry, the file %s does not exist. Please enter a valid filepath:\n' % filepath)

    # load the data
    data = load_data(filepath)

    # calculate
    # quickmaffs(data)
    quickmaffs2(data)
