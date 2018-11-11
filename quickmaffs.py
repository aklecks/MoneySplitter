import pandas as pd
import numpy as np
from timeit import default_timer

def quickmaffs(data):
    print('calculating..')
    start = default_timer()  # to time the function
    personenzahl = data.shape[1]
    summe = [sum(data['Person' + str(i)]) for i in range(personenzahl)]
    gesamtsumme = sum(summe)
    print('personenzahl: ', personenzahl)
    durchschnitt = np.mean(summe)
    print('durchschnitt: ', durchschnitt)
    differenz = summe - durchschnitt
    differenz2 = differenz.copy()
    print('differenz: ', differenz)
    sortiert = sorted(differenz)
    print('sortiert: ', sortiert)
    # welche person ist sortiert[i]
    oldpos = np.array([list(differenz).index(sortiert[i]) for i in range(personenzahl)])
    print('oldpos: ', oldpos)
    # richtige numerierung von leuten die gleichviel gezahlt haben
    i = 0
    while i in range(personenzahl-2):
        gleichzahlig = list(oldpos[i] - oldpos).count(0)
        for a in range(i, i + gleichzahlig):
            differenz2[oldpos[a]] += np.pi + a
            oldpos[a + 1] = list(differenz2).index(sortiert[a + 1])
        i += 1 + gleichzahlig

    print('oldpos after while: ', oldpos)

    # ausgabe
    a = 0
    ende = personenzahl - 1
    loop_count = 0
    while sortiert.count(0) <= personenzahl - 2:
        if sortiert[a] >= - 0.005:
            break
        if loop_count > ende:  # avoid endless loop
            print('!!FATAL ERROR!!')
            break
        if sortiert[a] + sortiert[ende] > 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differenz_rounded = -1 * np.around(differenz[oldpos[a]], decimals=2)
            # ausgabe
            print("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[ende]) + ": " + str(differenz_rounded))
            # änderung der übrigen beträge und sortierung
            differenz[oldpos[ende]] += differenz[oldpos[a]]
            v0 = differenz[oldpos[ende]]
            differenz[oldpos[a]] = 0.0
            sortiert = sorted(differenz)
            # permutierung von oldpos: erst 0-tes Element an die richtige Stelle, dann Endelement
            p0 = oldpos[0]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sortiert.index(0), p0)
            pe = oldpos[ende]
            oldpos = np.delete(oldpos, ende)
            oldpos = np.insert(oldpos, sortiert.index(v0), pe)

        elif sortiert[a] + sortiert[ende] < 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differenz_rounded = np.around(differenz[oldpos[ende]], decimals=2)
            # ausgabe
            print(("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[ende]) + ": " + str(differenz_rounded)))
            # änderung der übrigen beträge und sortierung
            differenz[oldpos[a]] += differenz[oldpos[ende]]
            v0 = differenz[oldpos[a]]
            differenz[oldpos[ende]] = 0.0
            sortiert = sorted(differenz)
            # permutierung von oldpos: erst Endelement an die richtige Stelle, dann 0-element
            pe = oldpos[ende]
            oldpos = np.delete(oldpos, ende)
            oldpos = np.insert(oldpos, sortiert.index(0), pe)
            p0 = oldpos[0]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sortiert.index(v0), p0)

        elif sortiert[a] + sortiert[ende] == 0 and sortiert[a] < 0:
            # zu überweisender betrag gerundet auf 2 dezimalstellen
            differenz_rounded = np.around(differenz[oldpos[ende]], decimals=2)
            # ausgabe
            print(("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[ende]) + ": " + str(differenz_rounded)))
            # änderung der jeweiligen Beträge auf 0
            differenz[oldpos[ende]] = 0.0
            differenz[oldpos[a]] = 0.0
            sortiert = sorted(differenz)
            # permutierung von oldpos
            p0 = oldpos[0]
            pe = oldpos[ende]
            oldpos = np.delete(oldpos, 0)
            oldpos = np.insert(oldpos, sortiert.index(0), p0)
            oldpos = np.delete(oldpos, ende)
            oldpos = np.insert(oldpos, sortiert.index(0), pe)

        loop_count += 1

    stop = default_timer()
    print('calculating took ', stop - start, ' seconds')