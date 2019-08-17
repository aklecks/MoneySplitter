import pandas as pd
import numpy as np
from timeit import default_timer


def quickmaffs2(data):
    print('calculating..')
    # TODO alle Variablennamen englisch machen, und einleuchtender
    start = default_timer()  # to time the function
    names_list = list(data.columns)
    num_persons = data.shape[1]
    sums_list = [sum(data[names_list[i]]) for i in range(num_persons)]
    mean = np.mean(sums_list)
    difference_array = np.array(sums_list - mean)

    print('Personenzahl: %s\nDurschnitt der Ausgaben: %f' % (num_persons, mean))
    print('\nDie folgenden Transaktionen werden vorgeschlagen:\n\n' + '-' * 50)
    for i in range(num_persons - 1):
        maxpos = np.argmax(difference_array)
        minpos = np.argmin(difference_array)
        if - difference_array.min() <= difference_array.max():
            difference_rounded = -1 * np.around(difference_array.min(), decimals=2)
            print('%s --> %s: %.2f' % (names_list[minpos], names_list[maxpos], difference_rounded))
            difference_array[maxpos] += difference_array.min()
            difference_array[minpos] = 0
        else:
            difference_rounded = np.around(difference_array.max(), decimals=2)
            print('%s --> %s: %.2f' % (names_list[minpos], names_list[maxpos], difference_rounded))
            difference_array[minpos] += difference_array.max()
            difference_array[maxpos] = 0
        i += 1

    stop = default_timer()
    print('-' * 50 + '\n\ncalculating took ', stop - start, ' seconds\n')

