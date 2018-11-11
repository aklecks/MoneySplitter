import pandas as pd


def load_data(filepath='data/testdata.csv'):
    '''
    load the data from csv file
    '''
    data = pd.read_csv(filepath)
    #print('data: \n', data)
    #print('erste spalte: \n', data['Person1'])
    #print('erste spalte zweiter eintrag: \n', data['Person1'][1])
    return data
