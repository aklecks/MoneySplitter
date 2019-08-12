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


def create_data(no_columns=5, no_rows=10, filename='bigdata.csv', use_real_names=True):
    """
    create a csv file with no_columns and no_rows
    """
    print('creating data..')

    filepath = os.path.join('data', filename)
    if use_real_names:
        # random names
        columns = ['Jaqueline', 'Chantal', 'Atomfried', 'Margarett', 'Jeana', 'Flavia', 'Kattie', 'Kendrick', 'Meghann', 'Sherika']
        # set number of columns
        no_columns = len(columns)
        # tell the user
        print('Attention: in this mode, the number of columns has to be exactly %i' % no_columns)
    else:
        columns = ['Person' + str(i) for i in range(no_columns)]

    # create array with random numbers
    random_array = np.random.randn(no_rows, no_columns)*40
    random_array = np.absolute(random_array)  # we want only positive values
    # make pandas dataframe
    data = pd.DataFrame(random_array, columns=columns)
    # make sure path exists
    os.makedirs('data', exist_ok=True)

    data.to_csv(filepath, index=False)



