import numpy as np
from timeit import default_timer


def quickmaffs(data):
    print('calculating..')
    # TODO alle Variablennamen englisch machen, und einleuchtender
    start = default_timer()  # to time the function
    names_list = list(data.columns)
    num_persons = data.shape[1]
    sums_list = [sum(data[names_list[i]]) for i in range(num_persons)]
    mean = np.mean(sums_list)
    difference_array = sums_list - mean  # TODO this is casted into numpy array, since mean is interpreted as numpy array
    difference_array2 = difference_array.copy()
    sorted_difference_list = sorted(difference_array)

    # Output of the basics
    print('Personenzahl: %s\nDurschnitt der Ausgaben: %f' % (num_persons, mean))

    # oldpos_array[i] corresponds to the position of the person in the
    # csv file whose postion is 'i' in the sorted_difference_list
    oldpos_array = np.array([list(difference_array).index(sorted_difference_list[i]) for i in range(num_persons)])

    # correct numbering of people with the same expenses
    i = 0
    while i in range(num_persons - 2):
        count_same_expenses = list(oldpos_array[i] - oldpos_array).count(0)
        for a in range(i, i + count_same_expenses):
            difference_array2[oldpos_array[a]] += np.pi + a
            oldpos_array[a + 1] = list(difference_array2).index(sorted_difference_list[a + 1])
        i += 1 + count_same_expenses

    # calculation
    a = 0
    end = num_persons - 1
    difference_rounded = 1  # just initialization
    loop_count = 0  # to count the number of loops
    print('\nDie folgenden Transaktionen werden vorgeschlagen:\n\n' + '-'*50)
    while sorted_difference_list.count(0) <= num_persons - 2:
        if loop_count > end:  # avoid endless loop
            print('!!FATAL ERROR!!')
            break
        if sorted_difference_list[a] + sorted_difference_list[end] > 0:
            # rounding the transaction value to 2 decimals
            difference_rounded = -1 * np.around(difference_array[oldpos_array[a]], decimals=2)
            # output
            print(names_list[oldpos_array[a]] + " -> " + names_list[oldpos_array[end]] + ": " + str(difference_rounded))
            # adjusting the pending transaction values and sorting them again
            difference_array[oldpos_array[end]] += difference_array[oldpos_array[a]]
            v0 = difference_array[oldpos_array[end]]
            difference_array[oldpos_array[a]] = 0.0
            sorted_difference_list = sorted(difference_array)
            # permutation of oldpos_array; first we change the first position, after that the last one
            p0 = oldpos_array[0]
            oldpos_array = np.delete(oldpos_array, 0)
            oldpos_array = np.insert(oldpos_array, sorted_difference_list.index(0), p0)
            pe = oldpos_array[end]
            oldpos_array = np.delete(oldpos_array, end)
            oldpos_array = np.insert(oldpos_array, sorted_difference_list.index(v0), pe)

        elif sorted_difference_list[a] + sorted_difference_list[end] < 0:
            # rounding the transaction value to 2 decimals
            difference_rounded = np.around(difference_array[oldpos_array[end]], decimals=2)
            # output
            print((names_list[oldpos_array[a]] + " -> " + names_list[oldpos_array[end]] + ": " + str(difference_rounded)))
            # adjusting the pending transaction values and sorting them again
            difference_array[oldpos_array[a]] += difference_array[oldpos_array[end]]
            v0 = difference_array[oldpos_array[a]]
            difference_array[oldpos_array[end]] = 0.0
            sorted_difference_list = sorted(difference_array)
            # permutation of oldpos_array; first we change the first position, after that the last one
            pe = oldpos_array[end]
            oldpos_array = np.delete(oldpos_array, end)
            oldpos_array = np.insert(oldpos_array, sorted_difference_list.index(0), pe)
            p0 = oldpos_array[0]
            oldpos_array = np.delete(oldpos_array, 0)
            oldpos_array = np.insert(oldpos_array, sorted_difference_list.index(v0), p0)

        elif sorted_difference_list[a] + sorted_difference_list[end] == 0 and sorted_difference_list[a] < 0:
            # rounding the transaction value to 2 decimals
            difference_rounded = np.around(difference_array[oldpos_array[end]], decimals=2)
            # output
            print((names_list[oldpos_array[a]] + " -> " + names_list[oldpos_array[end]] + ": " + str(difference_rounded)))
            # adjusting the corresponding values to 0
            difference_array[oldpos_array[end]] = 0.0
            difference_array[oldpos_array[a]] = 0.0
            sorted_difference_list = sorted(difference_array)
            # permutation of oldpos_array
            p0 = oldpos_array[0]
            pe = oldpos_array[end]
            oldpos_array = np.delete(oldpos_array, 0)
            oldpos_array = np.insert(oldpos_array, sorted_difference_list.index(0), p0)
            oldpos_array = np.delete(oldpos_array, end)
            oldpos_array = np.insert(oldpos_array, sorted_difference_list.index(0), pe)

        if difference_rounded < 0.005:
            break

        loop_count += 1
# TODO maybe add sanity check
    stop = default_timer()
    print('-'*50 + '\n\ncalculating took ', stop - start, ' seconds\n')
