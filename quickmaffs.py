import numpy as np
from timeit import default_timer


def quickmaffs(data):
    print('calculating..')
    start = default_timer()  # to time the function
    names_list = list(data.columns)  # lists the names of participants
    num_persons = data.shape[1]  # number of participants
    sums_list = list(data.loc['Sum'])  # sums of spent money (same index as names)
    mean = np.mean(sums_list)  # mean value of spent money
    difference_array = np.array(sums_list - mean)  # difference between spent money and mean value for each person

    print('Numper of participants: %s\nMean of the expenses: %.2f' % (num_persons, float(mean)))
    print('\nThe following transactions are recommended:\n\n' + '-' * 50)

    for i in range(num_persons - 1):
        maxpos = int(np.argmax(difference_array))  # position of the person who spent the most (after transaction)
        minpos = int(np.argmin(difference_array))  # position of the person who spent the least (after transaction)
        # to find the transaction value we take the rounded smaller number out of min and max of the difference array
        difference_rounded = float(np.around(min(-1 * difference_array.min(), difference_array.max()), decimals=2))
        # cutoff if rounded difference would be 0.00
        if difference_rounded < 0.009:
            break
        # case differentiation to see which person's sums will be changed by the transaction
        if - difference_array.min() <= difference_array.max():
            print('%s --> %s: %.2f' % (names_list[minpos], names_list[maxpos], difference_rounded))
            # transaction
            difference_array[maxpos] += difference_array.min()
            difference_array[minpos] = 0
        else:
            print('%s --> %s: %.2f' % (names_list[minpos], names_list[maxpos], difference_rounded))
            difference_array[minpos] += difference_array.max()
            difference_array[maxpos] = 0

    stop = default_timer()
    print('-' * 50 + '\n\ncalculating took %.8f seconds\n' % (stop - start))
