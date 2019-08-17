from help_functions import *
from quickmaffs import *

# TODO richtige Namen fuer Personen verwenden (Chris)
# TODO Einlesen von excel Tabelle
# TODO Ausgabe von Summen der Ausgaben der Teilnehmer jeweils + Differenz zum Durchschnitt (vermutlich am einfachsten als pandas Tabelle)
# TODO clean Code
# TODO option für Spalte mit Verwendungszwecken

print(os.getcwd())
filepath = 'data/bigdata.csv'
create_data(3000, 50)

data = load_data(filepath)

quickmaffs(data)
