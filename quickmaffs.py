import pandas as pd
import numpy as np
from help_functions import *


data = load_data()
summe = [sum(data['Person0']), sum(data['Person1']), sum(data['Person2']), sum(data['Person3']), sum(data['Person4'])]
gesamtsumme = sum(summe)
personenzahl = data.shape[1]
print(personenzahl)
durchschnitt = np.mean(summe)
print(durchschnitt)
differenz = summe - durchschnitt
differenz2 = differenz.copy()
print(differenz)
sortiert = sorted(differenz)
print(sortiert)
# welche person ist sortiert[i]
oldpos = np.array([list(differenz).index(sortiert[i]) for i in range(personenzahl)])
print(oldpos)
# richtige numerierung von leuten die gleichviel gezahlt haben
i = 0
while i in range(personenzahl-2):
    gleichzahlig = list(oldpos[i] - oldpos).count(0)
    for a in range(i, i + gleichzahlig):
        differenz2[oldpos[a]] += np.pi + a
        oldpos[a + 1] = list(differenz2).index(sortiert[a + 1])
    i += 1 + gleichzahlig
print(oldpos)

# ausgabe
print(differenz[0])
print(differenz)
a = 0
ende = personenzahl -1
while sortiert[a] < 0:
    if sortiert[a] + sortiert[ende] > 0:
        print(differenz[0])
        print("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[ende]) + ":" + str(differenz[oldpos[a]]))
        differenz[oldpos[a]] = 0
        differenz[oldpos[ende]] += differenz[oldpos[a]]
        sortiert = sorted(differenz)
        a += 1
    else:
        print(("Person " + str(oldpos[a]) + " -> Person " + str(oldpos[personenzahl]) + ": " + str(sortiert[personenzahl])))
        sortiert[personenzahl] = 0
        sortiert[a] += sortiert[personenzahl]
        sortiert = sorted(sortiert)
        a += 1


