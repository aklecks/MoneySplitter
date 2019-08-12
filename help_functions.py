import pandas as pd
import numpy as np
import os


def load_data(filepath='data/testdata.csv'):
    """
    load the data from csv file
    """
    print('loading data..')
    data = pd.read_csv(filepath)
    #print('data: \n', data)
    #print('erste spalte: \n', data['Person1'])
    #print('erste spalte zweiter eintrag: \n', data['Person1'][1])
    return data


def create_data(no_columns=5, no_rows=10, filename='bigdata.csv'):
    """
    create a csv file with no_columns and no_rows
    """
    print('creating data..')
    filepath = os.path.join('data', filename)
    random_array = np.random.randn(no_rows, no_columns)*40
    random_array = np.absolute(random_array)  # we want only positive values
    data = pd.DataFrame(random_array, columns=['Person'+str(i) for i in range(no_columns)])
    # make sure path exists
    os.makedirs('data', exist_ok=True)

    data.to_csv(filepath, index=False)



