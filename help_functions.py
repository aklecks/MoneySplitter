# load the data from csv file

import pandas as pd


def load_data(filepath='data/testdata.csv'):
    data = pd.read_csv(filepath)
    print(data)
    return data