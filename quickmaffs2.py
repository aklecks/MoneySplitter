import pandas as pd
import numpy as np
from timeit import default_timer


def quickmaffs2(data):
    print('calculating..')
    start = default_timer()             # to time the function
    names_list = list(data.columns)     # lists the names of participants
    num_persons = data.shape[1]         # number of participants
    sums_list = [sum(data[names_list[i]]) for i in range(num_persons)]  # sums of spent money (same index as names)
    mean = np.mean(sums_list)           # mean value of spent money
    difference_array = np.array(sums_list - mean)   # difference between spent money and mean value for each person

    print('Personenzahl: %s\nDurschnitt der Ausgaben: %f' % (num_persons, float(mean)))
    print('\nDie folgenden Transaktionen werden vorgeschlagen:\n\n' + '-' * 50)
    for i in range(num_persons - 1):
        maxpos = int(np.argmax(difference_array))       # position of the person who spent the most (after transaction)
        minpos = int(np.argmin(difference_array))       # position of the person who spent the least (after transaction)
        # to find the transaction value we take the rounded smaller number out of min and max of the difference array
        difference_rounded = float(np.around(min(-1 * difference_array.min(), difference_array.max()), decimals=2))
        if difference_rounded < 0.009:
            break
        if - difference_array.min() <= difference_array.max():
            print('%s --> %s: %.2f' % (names_list[minpos], names_list[maxpos], difference_rounded))
            difference_array[maxpos] += difference_array.min()
            difference_array[minpos] = 0
        else:
            print('%s --> %s: %.2f' % (names_list[minpos], names_list[maxpos], difference_rounded))
            difference_array[minpos] += difference_array.max()
            difference_array[maxpos] = 0
        i += 1

    stop = default_timer()
    print('-' * 50 + '\n\ncalculating took ', stop - start, ' seconds\n')

