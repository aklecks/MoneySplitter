import os
from argparse import ArgumentParser
from timeit import default_timer
from help_functions import load_data, create_data
from quickmaffs import quickmaffs

if __name__ == '__main__':
    start = default_timer()
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
    # create_data_flag = True

    if filepath is None:
        filepath = input('Please enter path to csv file: \n')

    if create_data_flag:
        create_data(3000, 500, use_real_names=False)
        filepath = 'data/bigdata.csv'

    # check if filepath is valid
    while not os.path.isfile(filepath):
        # tell them and get correct path
        filepath = input('Sorry, the file %s does not exist. Please enter a valid filepath:\n' % filepath)

    # load the data
    data = load_data(filepath)

    # calculate
    quickmaffs(data)

    # runtime
    stop = default_timer()
    print('total runtime: %.8f seconds\n' % (stop - start))
