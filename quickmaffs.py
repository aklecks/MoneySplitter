import pandas as pd
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
    difference_list = sums_list - mean  # TODO this is casted into numpy array, since mean is interpreted as numpy array
    difference_list2 = difference_list.copy()
    sorted_difference_list = sorted(difference_list)

    # Output of the basics
    print('Personenzahl: %s\nDurschnitt der Ausgaben: %f' % (num_persons, mean))

    # welche person ist sorted_difference_list[i]
    oldpos = np.array([list(difference_list).index(sorted_difference_list[i]) for i in range(num_persons)])

    # richtige numerierung von leuten die gleichviel gezahlt haben
    i = 0
    while i in range(num_persons - 2):
        count_same_expenses = list(oldpos[i] - oldpos).count(0)
        for a in range(i, i + count_same_expenses):
            difference_list2[oldpos[a]] += np.pi + a
            oldpos[a + 1] = list(difference_list2).index(sorted_difference_list[a + 1])
        i += 1 + count_same_expenses

    # calculation
    a = 0
    end = num_persons - 1
    differece_rounded = 1  # just initialization
    loop_count = 0  # to count the number of loops
    print('\nDie folgenden Transaktionen werden vorgeschlagen:\n\n' + '-'*50)
    while sorted_difference_list.count(0) <= num_persons - 2:
        if loop_count > end:  # avoid endless loop
            print('!!FATAL ERROR!!')
            break
        if sorted_difference_list[a] + sorted_difference_list[end] > 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differece_rounded = -1 * np.around(difference_list[oldpos[a]], decimals=2)
            # ausgabe
            print(names_list[oldpos[a]] + " -> " + names_list[oldpos[end]] + ": " + str(differece_rounded))
            # änderung der übrigen beträge und sortierung
            difference_list[oldpos[end]] += difference_list[oldpos[a]]
            v0 = difference_list[oldpos[end]]
            difference_list[oldpos[a]] = 0.0
            sorted_difference_list = sorted(difference_list)
            # permutierung von oldpos: erst 0-tes Element an die richtige Stelle, dann Endelement
            p0 = oldpos[0]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sorted_difference_list.index(0), p0)
            pe = oldpos[end]
            oldpos = np.delete(oldpos, end)
            oldpos = np.insert(oldpos, sorted_difference_list.index(v0), pe)

        elif sorted_difference_list[a] + sorted_difference_list[end] < 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differece_rounded = np.around(difference_list[oldpos[end]], decimals=2)
            # ausgabe
            print((names_list[oldpos[a]] + " -> " + names_list[oldpos[end]] + ": " + str(differece_rounded)))
            # änderung der übrigen beträge und sortierung
            difference_list[oldpos[a]] += difference_list[oldpos[end]]
            v0 = difference_list[oldpos[a]]
            difference_list[oldpos[end]] = 0.0
            sorted_difference_list = sorted(difference_list)
            # permutierung von oldpos: erst Endelement an die richtige Stelle, dann 0-element
            pe = oldpos[end]
            oldpos = np.delete(oldpos, end)
            oldpos = np.insert(oldpos, sorted_difference_list.index(0), pe)
            p0 = oldpos[0]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sorted_difference_list.index(v0), p0)

        elif sorted_difference_list[a] + sorted_difference_list[end] == 0 and sorted_difference_list[a] < 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differece_rounded = np.around(difference_list[oldpos[end]], decimals=2)
            # ausgabe
            print((names_list[oldpos[a]] + " -> " + names_list[oldpos[end]] + ": " + str(differece_rounded)))
            # änderung der jeweiligen Beträge auf 0
            difference_list[oldpos[end]] = 0.0
            difference_list[oldpos[a]] = 0.0
            sorted_difference_list = sorted(difference_list)
            # permutierung von oldpos
            p0 = oldpos[0]
            pe = oldpos[end]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sorted_difference_list.index(0), p0)
            oldpos = np.delete(oldpos, end)
            oldpos = np.insert(oldpos, sorted_difference_list.index(0), pe)

        if differece_rounded < 0.005:
            break

        loop_count += 1
# TODO maybe add sanity check
    stop = default_timer()
    print('-'*50 + '\n\ncalculating took ', stop - start, ' seconds\n')
