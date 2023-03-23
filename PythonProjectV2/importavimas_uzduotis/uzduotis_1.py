'''
1 užduotis
Python faile padaryti šiuos veiksmus (atskirai, ne iškart):

Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką (.now().time()).
Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.
Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.
'''


from datetime import date
from datetime import datetime
from datetime import datetime as now

print(datetime.now())
print(date.today())
print(now.today('%H %M %S'))

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)