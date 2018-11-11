import pandas as pd
import numpy as np
from help_functions import *


data = load_data()
summe = [sum(data['Person0']), sum(data['Person1']), sum(data['Person2']), sum(data['Person3']), sum(data['Person4'])]
gesamtsumme = sum(summe)
personenzahl = data.shape[1]
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
while sortiert.count(0) <= personenzahl - 2:
    if sortiert[a] + sortiert[ende] > 0:
        # runden auf 2 dezimalstellen
        differenz_rounded = -1 * np.around(differenz[oldpos[a]], decimals=2)
        print("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[ende]) + ": " + str(differenz_rounded))
        differenz[oldpos[ende]] += differenz[oldpos[a]]
        differenz[oldpos[a]] = 0
        sortiert = sorted(differenz)
        p0 = oldpos[0]
        oldpos = np.delete(oldpos, 0)
        oldpos = np.insert(oldpos, sortiert.index(0), p0)

    elif sortiert[a] + sortiert[ende] < 0:
        sortiert_rounded = np.around(sortiert[ende], decimals=2)
        print(("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[ende]) + ": " + str(sortiert_rounded)))
        sortiert[ende] = 0
        sortiert[a] += sortiert[ende]
        sortiert = sorted(sortiert)
        pe = oldpos[ende]
        oldpos = np.delete(oldpos, ende)
        oldpos = np.insert(oldpos, sortiert.index(0), pe)

    elif sortiert[a] + sortiert[ende] == 0 and sortiert[a] < 0:
        sortiert_rounded = np.around(sortiert[ende], decimals=2)
        print(("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[ende]) + ": " + str(sortiert_rounded)))
        sortiert[ende] = 0
        sortiert[0] = 0
        sortiert = sorted(sortiert)
        p0 = oldpos[0]
        pe = oldpos[ende]
        oldpos = np.delete(oldpos, 0)
        oldpos = np.insert(oldpos, sortiert.index(0), p0)
        oldpos = np.delete(oldpos, ende)
        oldpos = np.insert(oldpos, sortiert.index(0), pe)




