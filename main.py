from help_functions import *
from quickmaffs import *

filepath = 'Data/bigdata.csv'
create_data(3000, 50)

data = load_data(filepath)

quickmaffs(data)  # TODO: funktioniert oft nicht, wenn mehr als 5 spalten
