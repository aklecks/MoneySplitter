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
    difference = sums_list - mean  # TODO this is casted into numpy array, since mean is interpreted as numpy array
    difference2 = difference.copy()
    sortiert = sorted(difference)

    # Output of the basics
    print('Personenzahl: %s\nDurschnitt der Ausgaben: %f' % (num_persons, mean))

    # welche person ist sortiert[i]
    oldpos = np.array([list(difference).index(sortiert[i]) for i in range(num_persons)])

    # richtige numerierung von leuten die gleichviel gezahlt haben
    i = 0
    while i in range(num_persons - 2):
        gleichzahlig = list(oldpos[i] - oldpos).count(0)
        for a in range(i, i + gleichzahlig):
            difference2[oldpos[a]] += np.pi + a
            oldpos[a + 1] = list(difference2).index(sortiert[a + 1])
        i += 1 + gleichzahlig

    # calculation
    a = 0
    ende = num_persons - 1
    differenz_rounded = 1  # just initialization
    loop_count = 0  # to count the number of loops
    print('\nDie folgenden Transaktionen werden vorgeschlagen:\n\n' + '-'*50)
    while sortiert.count(0) <= num_persons - 2:
        if loop_count > ende:  # avoid endless loop
            print('!!FATAL ERROR!!')
            break
        if sortiert[a] + sortiert[ende] > 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differenz_rounded = -1 * np.around(difference[oldpos[a]], decimals=2)
            # ausgabe
            print(names_list[oldpos[a]] + " -> " + names_list[oldpos[ende]] + ": " + str(differenz_rounded))
            # änderung der übrigen beträge und sortierung
            difference[oldpos[ende]] += difference[oldpos[a]]
            v0 = difference[oldpos[ende]]
            difference[oldpos[a]] = 0.0
            sortiert = sorted(difference)
            # permutierung von oldpos: erst 0-tes Element an die richtige Stelle, dann Endelement
            p0 = oldpos[0]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sortiert.index(0), p0)
            pe = oldpos[ende]
            oldpos = np.delete(oldpos, ende)
            oldpos = np.insert(oldpos, sortiert.index(v0), pe)

        elif sortiert[a] + sortiert[ende] < 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differenz_rounded = np.around(difference[oldpos[ende]], decimals=2)
            # ausgabe
            print((names_list[oldpos[a]] + " -> " + names_list[oldpos[ende]] + ": " + str(differenz_rounded)))
            # änderung der übrigen beträge und sortierung
            difference[oldpos[a]] += difference[oldpos[ende]]
            v0 = difference[oldpos[a]]
            difference[oldpos[ende]] = 0.0
            sortiert = sorted(difference)
            # permutierung von oldpos: erst Endelement an die richtige Stelle, dann 0-element
            pe = oldpos[ende]
            oldpos = np.delete(oldpos, ende)
            oldpos = np.insert(oldpos, sortiert.index(0), pe)
            p0 = oldpos[0]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sortiert.index(v0), p0)

        elif sortiert[a] + sortiert[ende] == 0 and sortiert[a] < 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differenz_rounded = np.around(difference[oldpos[ende]], decimals=2)
            # ausgabe
            print((names_list[oldpos[a]] + " -> " + names_list[oldpos[ende]] + ": " + str(differenz_rounded)))
            # änderung der jeweiligen Beträge auf 0
            difference[oldpos[ende]] = 0.0
            difference[oldpos[a]] = 0.0
            sortiert = sorted(difference)
            # permutierung von oldpos
            p0 = oldpos[0]
            pe = oldpos[ende]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sortiert.index(0), p0)
            oldpos = np.delete(oldpos, ende)
            oldpos = np.insert(oldpos, sortiert.index(0), pe)

        if differenz_rounded < 0.005:
            break

        loop_count += 1
# TODO maybe add sanity check
    stop = default_timer()
    print('-'*50 + '\n\ncalculating took ', stop - start, ' seconds\n')
