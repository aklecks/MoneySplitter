import pandas as pd
import numpy as np
import os


def load_data(filepath='data/testdata.csv'):
    """
    load the data from csv file
    """
    print('loading data..')
    # get the column names (so we can drop those that we don't want)
    columns = list(pd.read_csv(filepath, nrows=1))
    # we don't want columns with empty names (since these are used for transaction purpose)
    columns_we_want = [col for col in columns if 'Unnamed' not in col]
    # read the data from file
    data = pd.read_csv(filepath, usecols=columns_we_want, dtype=float)
    # fill in NaN values with zero
    data.fillna(0, inplace=True)

    # print it out
    print('data: \n', data)
    return data


def create_data(num_persons, num_transactions, filename='bigdata.csv', use_real_names=True):
    """
    create a csv file with no_columns and no_rows
    """
    print('creating data..')

    filepath = os.path.join('data', filename)
    if use_real_names:
        # random names
        columns = ['Jaqueline', 'Chantal', 'Atomfried', 'Margarett', 'Jeana', 'Flavia', 'Kattie', 'Kendrick', 'Meghann', 'Sherika']
        # set number of columns
        num_persons = len(columns)
        # tell the user
        print('Attention: in this mode, the number of columns has to be exactly %i' % num_persons)
    else:
        columns = ['Person' + str(i) for i in range(num_persons)]

    # create array with random numbers
    random_array = np.random.randn(num_transactions, num_persons) * 40
    random_array = np.absolute(random_array)  # we want only positive values
    # make pandas dataframe
    data = pd.DataFrame(random_array, columns=columns)
    # make sure path exists
    os.makedirs('data', exist_ok=True)

    data.to_csv(filepath, index=False)



